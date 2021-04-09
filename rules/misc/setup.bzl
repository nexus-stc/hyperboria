"""
Setup various packages
"""

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive", "http_file")

def rules_misc_setup_internal():
    """
    Setup various packages
    """
    http_archive(
        name = "bazel_gazelle",
        sha256 = "d8c45ee70ec39a57e7a05e5027c32b1576cc7f16d9dd37135b0eddde45cf1b10",
        urls = [
            "https://storage.googleapis.com/bazel-mirror/github.com/bazelbuild/bazel-gazelle/releases/download/v0.20.0/bazel-gazelle-v0.20.0.tar.gz",
            "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.20.0/bazel-gazelle-v0.20.0.tar.gz",
        ],
    )

    http_archive(
        name = "com_github_bazelbuild_buildtools",
        sha256 = "3ef0caba290b88fb7f85a1d39397df990d8a819c405dde4439c09826274aca05",
        strip_prefix = "buildtools-e002736a9eca26c3356590213bff9292ca4af580",
        url = "https://github.com/bazelbuild/buildtools/archive/e002736a9eca26c3356590213bff9292ca4af580.zip",
    )

    http_archive(
        name = "com_github_google_flatbuffers",
        strip_prefix = "flatbuffers-04d80f255d1c2fa7a466e8465a119c0eaef26d59",
        urls = ["https://github.com/google/flatbuffers/archive/04d80f255d1c2fa7a466e8465a119c0eaef26d59.zip"],
    )

    http_archive(
        name = "com_github_grpc_grpc",
        sha256 = "f046d4cb4d60d4f2a2087e9d46c7ec0c523cd54ebf68eda6272de4ce65e20ac7",
        strip_prefix = "grpc-ae7f520358d7145a7484db693376fdebbd72662d",
        urls = [
            "https://github.com/grpc/grpc/archive/ae7f520358d7145a7484db693376fdebbd72662d.tar.gz",
        ],
    )

    http_archive(
        name = "com_google_protobuf",
        sha256 = "65e020a42bdab44a66664d34421995829e9e79c60e5adaa08282fd14ca552f57",
        strip_prefix = "protobuf-3.15.6",
        url = "https://github.com/protocolbuffers/protobuf/archive/v3.15.6.tar.gz",
    )

    http_archive(
        name = "ghostscript",
        build_file_content = 'exports_files(["gs-952-linux-x86_64"])',
        strip_prefix = "ghostscript-9.52-linux-x86_64",
        sha256 = "3c235f005d31a0747617d3628b2313396ececda9669dbceba9ebda531b903578",
        urls = ["https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs952/ghostscript-9.52-linux-x86_64.tgz"],
    )

    http_archive(
        name = "io_bazel_rules_go",
        sha256 = "db2b2d35293f405430f553bc7a865a8749a8ef60c30287e90d2b278c32771afe",
        urls = [
            "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.22.3/rules_go-v0.22.3.tar.gz",
            "https://github.com/bazelbuild/rules_go/releases/download/v0.22.3/rules_go-v0.22.3.tar.gz",
        ],
    )

    http_archive(
        name = "lz4",
        sha256 = "0b8bf249fd54a0b974de1a50f0a13ba809a78fd48f90c465c240ee28a9e4784d",
        build_file = "@//rules/misc:lz4.BUILD",
        strip_prefix = "lz4-1.9.2/lib",
        urls = ["https://github.com/lz4/lz4/archive/v1.9.2.zip"],
    )

    http_file(
        name = "mc",
        downloaded_file_path = "mc",
        sha256 = "e011de80e5a5cf23aa54207f4dbe68edd8d39e71783683ca9befc0345c9cf69d",
        urls = ["https://dl.min.io/client/mc/release/linux-amd64/archive/mc.RELEASE.2020-05-16T01-44-37Z"],
    )

    http_file(
        name = "pdfbox",
        downloaded_file_path = "pdfbox.jar",
        sha256 = "4485d9e6713f5b9c93824a0eb54e57717d3fd736244734c6276b65e17eab5cae",
        urls = ["https://mirror.linux-ia64.org/apache/pdfbox/2.0.23/pdfbox-app-2.0.23.jar"],
    )

    http_archive(
        name = "cities",
        sha256 = "3e720fc7249919ea340ff9c49c4423953278107e1f53a0e48f203f04851a3f7f",
        build_file_content = 'exports_files(["cities1000.txt"])',
        type = "zip",
        urls = ["https://drive.google.com/u/0/uc?id=14YTWJk477bXWMmXT1EgpXP0aIX_au-AA&export=download"],
    )
    http_archive(
        name = "openssl",
        sha256 = "9066c68c1aa8e8719af61cb82b88156ab07b3ad2a9ab1f874a8afb324583b1b6",
        build_file = "@//rules/misc:openssl.BUILD",
        strip_prefix = "openssl-OpenSSL_1_0_2m",
        url = "https://github.com/openssl/openssl/archive/OpenSSL_1_0_2m.tar.gz",
    )

    http_archive(
        name = "zlib",
        sha256 = "629380c90a77b964d896ed37163f5c3a34f6e6d897311f1df2a7016355c45eff",
        build_file = "@//rules/misc:zlib.BUILD",
        strip_prefix = "zlib-1.2.11",
        url = "https://github.com/madler/zlib/archive/v1.2.11.tar.gz",
    )

    http_archive(
        name = "unrar",
        sha256 = "a9521667094664084387baf17bcfe1d83a332f2b3b89736e8cb0de5e72fd7bdd",
        build_file_content = 'exports_files(["unrar"])',
        strip_prefix = "rar",
        urls = ["https://www.rarlab.com/rar/rarlinux-x64-5.9.0.tar.gz"],
    )
