"""
Common tools for NodeJS
"""

load("@build_bazel_rules_nodejs//:providers.bzl", "NpmPackageInfo")

def get_transitive_depsets(data):
    """
    It requires files from dependencies

    Args:
      data: data
    Returns:
      Separate depsets for native and NpmPackageInfo deps
    """
    depsets = []
    node_modules_depsets = []

    for d in data:
        if NpmPackageInfo in d:
            node_modules_depsets.append(d[NpmPackageInfo].sources)
        else:
            depsets.append(d[DefaultInfo].files)

    return depsets, node_modules_depsets

def _js_library_impl(ctx):
    depsets, node_modules_depsets = get_transitive_depsets(ctx.attr.data)
    trans_srcs = depset(ctx.files.srcs, transitive = depsets + node_modules_depsets)
    return [
        DefaultInfo(
            files = trans_srcs,
        ),
    ]

js_library = rule(
    implementation = _js_library_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = True),
        "data": attr.label_list(),
    },
)
