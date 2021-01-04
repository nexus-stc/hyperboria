"""JS build rules"""

load("//rules/nodejs:common.bzl", "get_transitive_depsets")

CONTENT_PREFIX = """
set -uo pipefail; f=bazel_tools/tools/bash/runfiles/runfiles.bash
source "${RUNFILES_DIR:-/dev/null}/$f" 2>/dev/null || \
source "$(grep -sm1 "^$f " "${RUNFILES_MANIFEST_FILE:-/dev/null}" | cut -f2- -d' ')" 2>/dev/null || \
source "$0.runfiles/$f" 2>/dev/null || \
source "$(grep -sm1 "^$f " "$0.runfiles_manifest" | cut -f2- -d' ')" 2>/dev/null || \
source "$(grep -sm1 "^$f " "$0.exe.runfiles_manifest" | cut -f2- -d' ')" 2>/dev/null || \
{ echo>&2 "ERROR: cannot find $f"; exit 1; }; f=; set -e
"""

WEBPACK_DEV_SERVER_WRAPPER_TEMPLATE = """
{webpack_dev_server_cmd} --config {webpack_config_file}
"""

CompiledInfo = provider(fields = ["compiled_files", "source_files"])

def _generate_server_js_impl(ctx):
    short_path = ctx.outputs.server_js.short_path
    short_path = short_path[:short_path.rfind("/")]
    ctx.actions.expand_template(
        template = ctx.file.template,
        output = ctx.outputs.server_js,
        substitutions = {
            "{config_path}": ctx.file.config.basename,
            "{webpack_config_path}": ctx.file.webpack_config.basename,
            "{static_path}": short_path + "/webpack_dist",
        },
    )

_generate_server_js = rule(
    implementation = _generate_server_js_impl,
    attrs = {
        "config": attr.label(mandatory = True, allow_single_file = True),
        "webpack_config": attr.label(allow_single_file = True),
        "template": attr.label(
            default = Label("//rules/nodejs:webpack.server.js"),
            allow_single_file = True,
        ),
    },
    outputs = {
        "server_js": "server.js",
    },
)

def _generate_webpack_dev_server_wrapper(ctx):
    webpack_dev_server_wrapper_content = WEBPACK_DEV_SERVER_WRAPPER_TEMPLATE.format(
        webpack_dev_server_cmd = ctx.attr._webpack_dev_server_binary.files_to_run.executable.short_path,
        webpack_config_file = ctx.file.webpack_config.short_path,
    )
    ctx.actions.write(
        ctx.outputs.webpack_dev_server_runner,
        CONTENT_PREFIX + webpack_dev_server_wrapper_content,
        is_executable = True,
    )

def _webpack_binary_impl(ctx):
    depsets, node_modules_depsets = get_transitive_depsets(ctx.attr.data)
    trans_srcs = depset(ctx.files.srcs + [ctx.file.config, ctx.file.webpack_config], transitive = depsets + node_modules_depsets)
    runfiles = ctx.runfiles(transitive_files = trans_srcs).merge(
        ctx.attr._webpack_dev_server_binary[DefaultInfo].default_runfiles,
    )

    _generate_webpack_dev_server_wrapper(ctx)

    return [
        DefaultInfo(
            executable = ctx.outputs.webpack_dev_server_runner,
            runfiles = runfiles,
            files = trans_srcs,
        ),
    ]

_webpack_binary = rule(
    implementation = _webpack_binary_impl,
    attrs = {
        "config": attr.label(mandatory = True, allow_single_file = True),
        "webpack_config": attr.label(mandatory = True, allow_single_file = True),
        "srcs": attr.label_list(allow_files = True),
        "data": attr.label_list(),
        "_webpack_binary": attr.label(
            default = Label("//rules/nodejs:webpack-binary"),
            executable = True,
            cfg = "host",
        ),
        "_webpack_dev_server_binary": attr.label(
            default = Label("//rules/nodejs:webpack-dev-server-binary"),
            executable = True,
            cfg = "host",
        ),
    },
    outputs = {
        "webpack_dev_server_runner": "webpack_dev_server_runner",
    },
    executable = True,
)

def _webpack_compile_impl(ctx):
    depsets, node_modules_depsets = get_transitive_depsets(ctx.attr.deps)
    trans_srcs = depset(ctx.files.srcs + [ctx.file.config, ctx.file.webpack_config], transitive = depsets + node_modules_depsets)
    runfiles = ctx.runfiles(transitive_files = trans_srcs).merge(
        ctx.attr._webpack_dev_server_binary[DefaultInfo].default_runfiles,
    )

    _generate_webpack_dev_server_wrapper(ctx)

    ctx.actions.run(
        inputs = trans_srcs,
        outputs = [ctx.outputs.webpack_dist],
        arguments = [
            "--mode",
            "production",
            "--config",
            ctx.file.webpack_config.short_path,
            "--output-path",
            ctx.outputs.webpack_dist.path,
        ],
        progress_message = "Compiling %s by Webpack..." % ctx.outputs.webpack_dist.short_path,
        executable = ctx.executable._webpack_binary,
    )

    return [
        DefaultInfo(
            executable = ctx.outputs.webpack_dev_server_runner,
            runfiles = runfiles,
            files = trans_srcs,
        ),
        CompiledInfo(
            compiled_files = depset([ctx.outputs.webpack_dist]),
            source_files = depset([ctx.file.config]),
        ),
    ]

_webpack_compile = rule(
    implementation = _webpack_compile_impl,
    attrs = {
        "config": attr.label(mandatory = True, allow_single_file = True),
        "webpack_config": attr.label(mandatory = True, allow_single_file = True),
        "srcs": attr.label_list(allow_files = True),
        "data": attr.label_list(),
        "_webpack_binary": attr.label(
            default = Label("//rules/nodejs:webpack-binary"),
            executable = True,
            cfg = "host",
        ),
        "_webpack_dev_server_binary": attr.label(
            default = Label("//rules/nodejs:webpack-dev-server-binary"),
            executable = True,
            cfg = "host",
        ),
    },
    outputs = {
        "webpack_dist": "webpack_dist",
        "webpack_dev_server_runner": "webpack_dev_server_runner",
    },
    executable = True,
)

def _webpack_data_impl(ctx):
    return [DefaultInfo(
        files = depset(
            transitive = [
                ctx.attr.compiled[CompiledInfo].compiled_files,
                ctx.attr.compiled[CompiledInfo].source_files,
            ],
        ),
    )]

_webpack_data = rule(
    implementation = _webpack_data_impl,
    attrs = {
        "compiled": attr.label(),
    },
)

def webpack_binary(
        name,
        config = "config.js",
        webpack_config = "webpack.config.js",
        srcs = [],
        data = []):
    _webpack_binary(
        name = name,
        config = config,
        webpack_config = webpack_config,
        srcs = srcs,
        data = data,
    )
    _generate_server_js(
        name = name + ".server.js",
        config = config,
        webpack_config = webpack_config,
        template = "//rules/nodejs:webpack.dynamic.server.js",
    )

def webpack_compile(
        name,
        config = "config.js",
        webpack_config = "webpack.config.js",
        srcs = [],
        data = []):
    _webpack_compile(
        name = name,
        config = config,
        webpack_config = webpack_config,
        srcs = srcs,
        data = data,
    )
    _webpack_data(name = name + ".compiled", compiled = name)
    _generate_server_js(
        name = name + ".server.js",
        config = config,
        webpack_config = webpack_config,
    )
