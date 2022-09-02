"""
Setup various packages
"""

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

def rules_misc_setup_internal():
    """
    Setup various packages
    """

    http_archive(
        name = "com_github_bazelbuild_buildtools",
        sha256 = "3ef0caba290b88fb7f85a1d39397df990d8a819c405dde4439c09826274aca05",
        strip_prefix = "buildtools-e002736a9eca26c3356590213bff9292ca4af580",
        url = "https://github.com/bazelbuild/buildtools/archive/e002736a9eca26c3356590213bff9292ca4af580.zip",
    )

    http_archive(
        name = "com_github_grpc_grpc",
        strip_prefix = "grpc-1.46.3",
        urls = [
            "https://github.com/grpc/grpc/archive/v1.46.3.tar.gz",
        ],
    )

    http_archive(
        name = "com_google_protobuf",
        strip_prefix = "protobuf-3.21.1",
        url = "https://github.com/protocolbuffers/protobuf/archive/v3.21.1.tar.gz",
    )
