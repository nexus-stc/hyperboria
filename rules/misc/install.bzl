"""
Install various packages
"""

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")
load("@com_github_bazelbuild_buildtools//buildifier:deps.bzl", "buildifier_dependencies")

def rules_misc_install_internal():
    """
    Install various packages
    """
    buildifier_dependencies()
    protobuf_deps()
