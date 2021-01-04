"""JS build rules"""

load("@build_bazel_rules_nodejs//:index.bzl", "nodejs_binary")
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

NUXT_WRAPPER_TEMPLATE = """
{nuxt_cmd} --config-file {nuxt_config_file}
"""

CompiledInfo = provider(fields = ["compiled_files", "source_files"])

def _generate_server_js_impl(ctx):
    ctx.actions.expand_template(
        template = ctx.file._template,
        output = ctx.outputs.server_js,
        substitutions = {
            "{config_file}": ctx.file.config.basename,
            "{nuxt_config_file}": ctx.file.nuxt_config.basename,
        },
    )

_generate_server_js = rule(
    implementation = _generate_server_js_impl,
    attrs = {
        "config": attr.label(mandatory = True, allow_single_file = True),
        "nuxt_config": attr.label(mandatory = True, allow_single_file = True),
        "_template": attr.label(
            default = Label("//rules/nodejs:nuxt.server.js"),
            allow_single_file = True,
        ),
    },
    outputs = {
        "server_js": "server.js",
    },
)

def _nuxt_compile_impl(ctx):
    depsets, node_modules_depsets = get_transitive_depsets(ctx.attr.data)
    trans_srcs = depset([ctx.file.nuxt_config], transitive = depsets + node_modules_depsets)
    source_files = depset([ctx.file.nuxt_config], transitive = depsets)
    runfiles = ctx.runfiles(transitive_files = trans_srcs).merge(
        ctx.attr.nuxt_binary[DefaultInfo].default_runfiles,
    )

    nuxt_wrapper_content = NUXT_WRAPPER_TEMPLATE.format(
        nuxt_cmd = ctx.attr.nuxt_binary.files_to_run.executable.short_path,
        nuxt_config_file = ctx.file.nuxt_config.short_path,
    )
    ctx.actions.write(ctx.outputs.nuxt_runner, CONTENT_PREFIX + nuxt_wrapper_content, is_executable = True)

    ctx.actions.run(
        inputs = trans_srcs,
        outputs = [ctx.outputs.nuxt_dist],
        arguments = [
            "build",
            "--standalone",
            "--build-dir=" + ctx.outputs.nuxt_dist.path,
            "--config-file",
            ctx.file.nuxt_config.short_path,
        ],
        progress_message = "Compiling %s by nuxtJS..." % ctx.outputs.nuxt_dist.short_path,
        executable = ctx.executable.nuxt_binary,
    )

    return [
        DefaultInfo(
            executable = ctx.outputs.nuxt_runner,
            runfiles = runfiles,
            files = trans_srcs,
        ),
        CompiledInfo(
            compiled_files = depset([ctx.outputs.nuxt_dist]),
            source_files = source_files,
        ),
    ]

_nuxt_compile = rule(
    implementation = _nuxt_compile_impl,
    attrs = {
        "nuxt_config": attr.label(mandatory = True, allow_single_file = True),
        "config": attr.label(mandatory = True, allow_single_file = True),
        "data": attr.label_list(),
        "nuxt_binary": attr.label(
            default = Label("//rules/nodejs:nuxt-binary"),
            executable = True,
            cfg = "host",
        ),
    },
    outputs = {
        "nuxt_dist": "nuxt_dist",
        "nuxt_runner": "nuxt_runner",
    },
    executable = True,
)

def _nuxt_data_impl(ctx):
    return [DefaultInfo(
        files = depset(
            transitive = [
                ctx.attr.compiled[CompiledInfo].compiled_files,
                ctx.attr.compiled[CompiledInfo].source_files,
            ],
        ),
    )]

_nuxt_data = rule(
    implementation = _nuxt_data_impl,
    attrs = {
        "compiled": attr.label(),
    },
)

def nuxt_compile(name, config = "config.js", nuxt_config = "nuxt.config.js", data = []):
    """
    Compile nuxt and produce files in CompiledInfo provider

    Args:
      name: name of the target, also name.nuxt-binary
      config: path to application config
      nuxt_config: path to nuxt config
      data: list of dependencies
    Returns:
      Produces outputs
    """
    nuxt_binary_name = name + ".nuxt-binary"
    nodejs_binary(
        name = nuxt_binary_name,
        entry_point = "@npm//:node_modules/nuxt/bin/nuxt.js",
        data = data,
        visibility = ["//visibility:public"],
    )
    _nuxt_compile(
        name = name,
        config = config,
        nuxt_config = nuxt_config,
        data = data,
        nuxt_binary = nuxt_binary_name,
    )
    _nuxt_data(name = name + ".compiled", compiled = name)
    _generate_server_js(
        name = name + ".server.js",
        config = config,
        nuxt_config = nuxt_config,
    )
