"""Module contains functions for package creation, publishing and deployment

Example:

    You could easily create target for debian package. It will make available :deb and :publish targets

        debian_package(
            name = "debian-repo",
            config_srcs = ["debian/debian-repo.aptly"],
            depends = [
                "nginx",
                "aptly",
            ],
            description = "Debian Repository Package",
            extra_postinst = [
                "aptly -config='/etc/debian-repo/debian-repo.aptly' repo create bionic -distribution=bionic -component=main || /bin/true",
                "aptly -config='/etc/debian-repo/debian-repo.aptly' publish repo bionic || /bin/true",
            ],
            package = "debian-repo",
            package_dir = "/var/cache/aptly",
            version = "1.0.0",
        )

    Then, you can

        bazel build :deb
        bazel run :publish
"""

load("@rules_pkg//:pkg.bzl", "pkg_tar")

tar_filetype = [".tar", ".tar.gz", ".tgz", ".tar.xz", ".tar.bz2"]
deb_filetype = [".deb", ".udeb"]

default_maintainer = "developers@example.com"

strip_prefix_by_action = {
    None: None,
    "repository": "/",
    "local": "./",
}

ScriptsInfo = provider(fields = ["postinst", "postrm", "preinst", "prerm"])

def deploy_command(deb_package, hostname, username = "pasha"):
    """Command for start deployment on `target_hosts` of package.

    Args:

        deb_package (File): Debian package to install
        hostname (str): host for installation
        username (str): SSH user for installation process

    Returns:

        Prepared string containing full bash command to start a deployment

    """
    echo = 'echo "Deploying to {hostname}"\n'
    remove_old = "ssh {username}@{hostname} 'sudo rm -f {package_name}'\n"
    copy = "scp {package_path} {username}@{hostname}:~\n"
    remote_install = "sudo -H apt install --reinstall ./{package_name}".format(package_name = deb_package.basename)
    notify = "ssh {username}@{hostname} '{remote_notify}'\n"
    install = "ssh {username}@{hostname} '{remote_install}'\n"
    return (echo + remove_old + copy + install + remove_old).format(
        package_name = deb_package.basename,
        package_path = deb_package.short_path,
        hostname = hostname,
        username = username,
        remote_install = remote_install,
    )

def _deploy(ctx):
    package = None

    for package in ctx.files.package:
        if package.basename.endswith(".deb") and package.basename != "deb.deb":
            break
    if not package:
        fail("No suitable debian package found!")

    content = "#!/usr/bin/env bash\nset -e\n"
    for target_host in ctx.attr.target_hosts:
        cmd = deploy_command(package, target_host)
        content += cmd
    ctx.actions.write(
        output = ctx.outputs.executable,
        content = content,
        is_executable = True,
    )
    runfiles = ctx.runfiles(
        files = [package],
        collect_default = True,
    )
    return [DefaultInfo(runfiles = runfiles)]

deploy = rule(
    implementation = _deploy,
    attrs = {
        "package": attr.label(allow_files = True),
        "target_hosts": attr.string_list(mandatory = True),
    },
    executable = True,
)

def _generate_scripts_impl(ctx):
    generator = {
        "postinst": {"template": ctx.file._postinst_template, "output": ctx.outputs.postinst},
        "postrm": {"template": ctx.file._postrm_template, "output": ctx.outputs.postrm},
        "preinst": {"template": ctx.file._preinst_template, "output": ctx.outputs.preinst},
        "prerm": {"template": ctx.file._prerm_template, "output": ctx.outputs.prerm},
    }
    overriden_basenames = {x.basename: x for x in ctx.files.overriden_scripts}
    for script in generator:
        if script in overriden_basenames:
            ctx.actions.run_shell(
                command = "cp %s %s" % (overriden_basenames[script].path, generator[script]["output"].path),
                inputs = [overriden_basenames[script]],
                outputs = [generator[script]["output"]],
            )
        else:
            args = [generator[script]["template"].path, generator[script]["output"].path]
            args.extend(["--name", ctx.attr.package_name])
            if ctx.attr.extra_postinst:
                args.extend(["--extra-postinst", "[" + ", ".join([escape(x) for x in ctx.attr.extra_postinst]) + ", ]"])
            if ctx.attr.services:
                args.extend(["--services", "[" + ", ".join([escape(x) for x in ctx.attr.services]) + ", ]"])
            if ctx.attr.add_user:
                args.extend(["--add-user", ctx.attr.add_user])
            if ctx.attr.user_groups:
                args.extend(["--user-groups", "[" + ", ".join([escape(x) for x in ctx.attr.user_groups]) + ", ]"])
            ctx.actions.run(
                executable = ctx.executable.jinja2,
                arguments = args,
                inputs = [generator[script]["template"]],
                outputs = [generator[script]["output"]],
                mnemonic = "jinja2",
            )
    return [ScriptsInfo(
        postinst = ctx.outputs.postinst,
        postrm = ctx.outputs.postrm,
        preinst = ctx.outputs.preinst,
        prerm = ctx.outputs.prerm,
    )]

generate_scripts = rule(
    implementation = _generate_scripts_impl,
    attrs = {
        "package_name": attr.string(mandatory = True),
        "services": attr.string_list(),
        "extra_postinst": attr.string_list(),
        "add_user": attr.string(),
        "user_groups": attr.string_list(),
        "overriden_scripts": attr.label_list(allow_files = True),
        "jinja2": attr.label(
            default = Label("//tools:jinja2"),
            cfg = "host",
            executable = True,
            allow_files = True,
        ),
        "_postinst_template": attr.label(
            default = Label("//rules/packaging/templates:postinst.jinja2"),
            allow_single_file = True,
        ),
        "_postrm_template": attr.label(
            default = Label("//rules/packaging/templates:postrm.jinja2"),
            allow_single_file = True,
        ),
        "_preinst_template": attr.label(
            default = Label("//rules/packaging/templates:preinst.jinja2"),
            allow_single_file = True,
        ),
        "_prerm_template": attr.label(
            default = Label("//rules/packaging/templates:prerm.jinja2"),
            allow_single_file = True,
        ),
    },
    outputs = {
        "postinst": "%{package_name}.postinst",
        "postrm": "%{package_name}.postrm",
        "preinst": "%{package_name}.preinst",
        "prerm": "%{package_name}.prerm",
    },
)

def _pkg_deb_impl(ctx):
    """The implementation for the pkg_deb rule."""
    files = [ctx.file.data]
    args = [
        "--output=" + ctx.outputs.deb.path,
        "--changes=" + ctx.outputs.changes.path,
        "--data=" + ctx.file.data.path,
        "--package=" + ctx.attr.package,
        "--architecture=" + ctx.attr.architecture,
        "--maintainer=" + ctx.attr.maintainer,
    ]

    if ctx.attr.scripts:
        args.append("--preinst=@" + ctx.attr.scripts[ScriptsInfo].preinst.path)
        files.append(ctx.attr.scripts[ScriptsInfo].preinst)
        args.append("--postinst=@" + ctx.attr.scripts[ScriptsInfo].postinst.path)
        files.append(ctx.attr.scripts[ScriptsInfo].postinst)
        args.append("--prerm=@" + ctx.attr.scripts[ScriptsInfo].prerm.path)
        files.append(ctx.attr.scripts[ScriptsInfo].prerm)
        args.append("--postrm=@" + ctx.attr.scripts[ScriptsInfo].postrm.path)
        files.append(ctx.attr.scripts[ScriptsInfo].postrm)

    # Conffiles can be specified by a file or a string list
    if ctx.attr.conffiles_file:
        if ctx.attr.conffiles:
            fail("Both conffiles and conffiles_file attributes were specified")
        args.append("--conffile=@" + ctx.file.conffiles_file.path)
        files.append(ctx.file.conffiles_file)
    elif ctx.attr.conffiles:
        args += ["--conffile=%s" % cf for cf in ctx.attr.conffiles]

    # Version and description can be specified by a file or inlined
    if ctx.attr.version_file:
        if ctx.attr.version:
            fail("Both version and version_file attributes were specified")
        args.append("--version=@" + ctx.file.version_file.path)
        files.append(ctx.file.version_file)
    elif ctx.attr.version:
        args.append("--version=" + ctx.attr.version)
    else:
        fail("Neither version_file nor version attribute was specified")

    if ctx.attr.description_file:
        if ctx.attr.description:
            fail("Both description and description_file attributes were specified")
        args.append("--description=@" + ctx.file.description_file.path)
        files.append(ctx.file.description_file)
    elif ctx.attr.description:
        args.append("--description=" + ctx.attr.description)
    else:
        fail("Neither description_file nor description attribute was specified")

    # Built using can also be specified by a file or inlined (but is not mandatory)
    if ctx.attr.built_using:
        args.append("--built_using=" + ctx.attr.built_using)

    if ctx.attr.priority:
        args.append("--priority=" + ctx.attr.priority)
    if ctx.attr.section:
        args.append("--section=" + ctx.attr.section)
    if ctx.attr.homepage:
        args.append("--homepage=" + ctx.attr.homepag)

    args.append("--distribution=" + ctx.attr.distribution)
    args.append("--urgency=" + ctx.attr.urgency)
    args += ["--depends=" + d for d in ctx.attr.depends]
    args += ["--suggests=" + d for d in ctx.attr.suggests]
    args += ["--enhances=" + d for d in ctx.attr.enhances]
    args += ["--conflicts=" + d for d in ctx.attr.conflicts]
    args += ["--pre_depends=" + d for d in ctx.attr.predepends]
    args += ["--recommends=" + d for d in ctx.attr.recommends]
    args += ["--replaces=" + d for d in ctx.attr.replaces]

    ctx.actions.run(
        executable = ctx.executable.make_deb,
        arguments = args,
        inputs = files,
        outputs = [ctx.outputs.deb, ctx.outputs.changes],
        mnemonic = "MakeDeb",
    )

# A rule for creating a deb file, see README.md
pkg_deb = rule(
    implementation = _pkg_deb_impl,
    attrs = {
        "data": attr.label(mandatory = True, allow_single_file = True),
        "package": attr.string(mandatory = True),
        "architecture": attr.string(default = "all"),
        "distribution": attr.string(default = "unstable"),
        "urgency": attr.string(default = "medium"),
        "maintainer": attr.string(mandatory = True),
        "scripts": attr.label(mandatory = False),
        "conffiles_file": attr.label(allow_single_file = True),
        "conffiles": attr.string_list(default = []),
        "version_file": attr.label(allow_single_file = True),
        "version": attr.string(),
        "description_file": attr.label(allow_single_file = True),
        "description": attr.string(),
        "built_using": attr.string(),
        "priority": attr.string(),
        "section": attr.string(),
        "homepage": attr.string(),
        "depends": attr.string_list(default = []),
        "suggests": attr.string_list(default = []),
        "enhances": attr.string_list(default = []),
        "conflicts": attr.string_list(default = []),
        "predepends": attr.string_list(default = []),
        "recommends": attr.string_list(default = []),
        "replaces": attr.string_list(default = []),

        # Implicit dependencies.
        "make_deb": attr.label(
            default = Label("//rules/packaging:make_deb"),
            cfg = "host",
            executable = True,
            allow_files = True,
        ),
    },
    outputs = {
        "deb": "%{package}_%{version}_%{architecture}.deb",
        "changes": "%{package}_%{version}_%{architecture}.changes",
    },
    executable = False,
)

def escape(x):
    return '"%s"' % x

def _get_extensions():
    extensions = {
        ".cron": "./etc/cron.d/",
        ".logrotate": "./etc/logrotate.d/",
        ".service": "./etc/systemd/system/",
    }

    debian_files = native.glob(["debian/**"])

    overriden_scripts = []
    content = {}
    symlinks = {}
    files_by_extension = {}
    services = []

    for filepath in debian_files:
        if filepath in ["debian/postinst", "debian/preinst", "debian/prerm", "debian/postrm"]:
            overriden_scripts.append(filepath)

        filename = filepath[(filepath.rfind("/") + 1):]
        last_dot = filepath.rfind(".")
        fileext = filepath[last_dot:]
        filepath_without_extension = filepath[:last_dot]
        filename_without_extension = filepath_without_extension[(filepath_without_extension.rfind("/") + 1):]

        if fileext in extensions:
            content.setdefault(extensions[fileext], []).append(filepath)

        # Cron-specific hack reasoned by these fucking monkeys restricting dots in the names of crontab files
        if fileext == ".cron":
            symlinks[extensions[".cron"] + filename_without_extension] = "./" + filename

        if fileext == ".service":
            services.append(filename_without_extension)

    return {"content": content, "overriden_scripts": overriden_scripts, "services": services, "symlinks": symlinks}

def debian_package(
        package_name,
        version,
        maintainer = default_maintainer,
        architecture = "amd64",
        description = None,
        homepage = None,
        depends = [],
        replaces = [],
        conflicts = [],
        content = None,
        symlinks = {},
        owner = None,
        mode = None,
        owners = {},
        modes = {},
        extra_postinst = [],
        target_hosts = [],
        visibility = None):
    """Package creation, publishing and deployment targets

    Args:
        package_name (str): debian package name. Defaults to default_company_name + '-' + name
        version (str): package version

        maintainer (str): maintainer email
        architecture (str): package architecture
        description (str): package description
        homepage (str): package homepage

        depends (list): debian packages a created package depends on
        replaces (list): debian packages a created package replaces
        conflicts (list): debian packages a created package conflicts to

        content (dict):
        symlinks (dict):
        owner (str):
        mode (str):
        owners (dict):
        modes (dict):

        extra_postinst (list):
        target_hosts (list):
        visibility (list):
    """

    all_tars = []

    extensions = _get_extensions()

    if content == None:
        content = {}

    content.update(extensions["content"])

    for path in content:
        tar_name = package_name + "-" + path.replace("/", "-")
        unstructured_tar_name = "unstructured-" + tar_name

        content_for_path = content[path]

        unstructured_content = [x for x in content_for_path if type(x) == "string"]
        structured_content = [x for x in content_for_path if type(x) == "dict"]

        pkg_tar(
            name = unstructured_tar_name,
            extension = "tar",
            package_dir = path,
            srcs = unstructured_content,
            empty_dirs = [path] if not content_for_path else [],
            ownername = owner,
            mode = mode,
            ownernames = owners,
            modes = modes,
        )
        all_tars.append(unstructured_tar_name)

        for i, el in enumerate(structured_content):
            keep_structure = el.get("keep_structure", None)
            strip_prefix = strip_prefix_by_action[keep_structure]

            subtar_name = "structured-" + tar_name + "-" + str(i)

            pkg_tar(
                name = subtar_name,
                extension = "tar",
                package_dir = path,
                srcs = el["srcs"],
                strip_prefix = strip_prefix,
                ownername = owner,
                mode = mode,
                ownernames = owners,
                modes = modes,
            )
            all_tars.append(subtar_name)

    scripts_target_name = package_name + "-scripts"
    generate_scripts(
        name = scripts_target_name,
        package_name = package_name,
        services = extensions["services"],
        extra_postinst = extra_postinst,
        overriden_scripts = extensions["overriden_scripts"],
    )
    data_tar_name = package_name + "-data-tar"

    symlinks = {"." + k.lstrip("."): v for k, v in symlinks.items()}
    symlinks.update(extensions["symlinks"])

    pkg_tar(
        name = data_tar_name,
        deps = all_tars,
        symlinks = symlinks,
        visibility = visibility,
    )

    pkg_deb(
        name = package_name + ".deb",
        package = package_name,
        version = version,
        maintainer = maintainer,
        architecture = architecture,
        description = description,
        homepage = homepage,
        depends = depends,
        replaces = replaces,
        conflicts = conflicts,
        data = data_tar_name,
        scripts = scripts_target_name,
        built_using = "bazel",
        visibility = visibility,
    )

    deploy(
        name = package_name + "-deploy",
        package = package_name + ".deb",
        target_hosts = target_hosts,
    )

def pkg_files(
        name,
        srcs,
        symlinks = {},
        owner = "0.0",
        ownername = None,
        mode = "0555",
        owners = {},
        ownernames = {},
        modes = {},
        visibility = None):
    """Package creation, publishing and deployment targets

    Args:
        name (str): name

        srcs (dict):
        symlinks (dict):
        owner (str):
        ownername (str):
        mode (str):
        owners (dict):
        ownernames (dict):
        modes (dict):
        visibility (dict):
    """

    all_tars = []
    for path in srcs:
        tar_name = name + path.replace("/", "-")

        partial_owner = owner
        partial_ownername = ownername
        partial_mode = mode

        if path in owners:
            partial_owner = owners[path]
        if path in ownernames:
            partial_ownername = ownernames[path]
        if path in modes:
            partial_mode = modes[path]

        pkg_tar(
            name = tar_name,
            extension = "tar",
            package_dir = path,
            srcs = srcs[path],
            empty_dirs = [path] if not srcs[path] else [],
            owner = partial_owner,
            ownername = partial_ownername,
            mode = partial_mode,
            strip_prefix = "./",
        )
        all_tars.append(tar_name)
    symlinks = {"." + k.lstrip("."): v for k, v in symlinks.items()}
    pkg_tar(
        name = name,
        deps = all_tars,
        symlinks = symlinks,
        owner = owner,
        ownername = ownername,
        mode = mode,
        owners = owners,
        ownernames = ownernames,
        modes = modes,
        visibility = visibility,
    )
