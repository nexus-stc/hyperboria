workspace(
    name = "hyperboria",
    managed_directories = {"@npm": ["rules/nodejs/node_modules"]},
)

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "11b0e65ec07113b2ea81be554c7471bb80fc5766aba6239c91d071602c46d50f",
    strip_prefix = "bazel-skylib-dc080e95161964a1ff841bfd0b871a1123c027a8",
    urls = [
        "https://github.com/bazelbuild/bazel-skylib/archive/dc080e95161964a1ff841bfd0b871a1123c027a8.tar.gz",
    ],
)

http_archive(
    name = "build_bazel_rules_nodejs",
    sha256 = "6142e9586162b179fdd570a55e50d1332e7d9c030efd853453438d607569721d",
    urls = ["https://github.com/bazelbuild/rules_nodejs/releases/download/3.0.0/rules_nodejs-3.0.0.tar.gz"],
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
    sha256 = "d0f5f605d0d656007ce6c8b5a82df3037e1d8fe8b121ed42e536f569dec16113",
    strip_prefix = "protobuf-3.14.0",
    urls = [
        "https://github.com/protocolbuffers/protobuf/archive/v3.14.0.tar.gz",
    ],
)

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "df3ef4a4b53b0145c9751c1e2a840f900e322e7798612a46257abe285d046dc5",
    strip_prefix = "rules_docker-7da0de3d094aae5601c45ae0855b64fb2771cd72",
    urls = [
        "https://github.com/bazelbuild/rules_docker/archive/7da0de3d094aae5601c45ae0855b64fb2771cd72.zip",
    ],
)

http_archive(
    name = "io_bazel_rules_k8s",
    sha256 = "95addfd2b7b07b5a4e75663d15aa57dc271f7b831ec404109322288e1b6bf126",
    strip_prefix = "rules_k8s-9f9886c7252d66bb2e2206842b149a6ceebe6fe5",
    urls = [
        "https://github.com/bazelbuild/rules_k8s/archive/9f9886c7252d66bb2e2206842b149a6ceebe6fe5.zip",
    ],
)

http_archive(
    name = "io_bazel_rules_rust",
    sha256 = "50a772198877e21a61823fa292d28539f8bc99d72463e55b5b09942394ec370e",
    strip_prefix = "rules_rust-9a8ef691b8e8f682d767189c38339cbee16d0a16",
    urls = [
        # Master branch as of 2020-10-16
        "https://github.com/bazelbuild/rules_rust/archive/9a8ef691b8e8f682d767189c38339cbee16d0a16.tar.gz",
    ],
)

http_archive(
    name = "rules_jvm_external",
    sha256 = "d85951a92c0908c80bd8551002d66cb23c3434409c814179c0ff026b53544dab",
    strip_prefix = "rules_jvm_external-3.3",
    urls = [
        "https://github.com/bazelbuild/rules_jvm_external/archive/3.3.zip",
    ],
)

http_archive(
    name = "rules_pkg",
    sha256 = "0a33148c4957e666a29443f75b2c0db1fe3e0baf7256742fc47a35731f7a1d2e",
    strip_prefix = "rules_pkg-4b0b9f4679484f107f750a60190ff5ec6b164a5f/pkg",
    urls = [
        "https://github.com/bazelbuild/rules_pkg/archive/4b0b9f4679484f107f750a60190ff5ec6b164a5f.zip",
    ],
)

http_archive(
    name = "rules_proto",
    sha256 = "aa1ee19226f707d44bee44c720915199c20c84a23318bb0597ed4e5c873ccbd5",
    strip_prefix = "rules_proto-40298556293ae502c66579620a7ce867d5f57311",
    urls = [
        "https://github.com/bazelbuild/rules_proto/archive/40298556293ae502c66579620a7ce867d5f57311.tar.gz",
    ],
)

http_archive(
    name = "rules_python",
    sha256 = "b228318a786d99b665bc83bd6cdb81512cae5f8eb15e8cd19f9956604b8939f5",
    strip_prefix = "rules_python-a4a1ccffc666db5376342789ad021a943fb84256",
    urls = [
        "https://github.com/bazelbuild/rules_python/archive/a4a1ccffc666db5376342789ad021a943fb84256.tar.gz",
    ],
)

http_archive(
    name = "subpar",
    sha256 = "e6e4332bf9af36c4165ad6cc7b2c76288e9f156eba35dc95b739e58c46f30a50",
    strip_prefix = "subpar-9fae6b63cfeace2e0fb93c9c1ebdc28d3991b16f",
    urls = [
        "https://github.com/google/subpar/archive/9fae6b63cfeace2e0fb93c9c1ebdc28d3991b16f.zip",
    ],
)

http_archive(
    name = "cython",
    build_file = "@com_github_grpc_grpc//third_party:cython.BUILD",
    sha256 = "e2e38e1f0572ca54d6085df3dec8b607d20e81515fb80215aed19c81e8fe2079",
    strip_prefix = "cython-0.29.21",
    urls = [
        "https://github.com/cython/cython/archive/0.29.21.tar.gz",
    ],
)

# Java

load("//rules/java:artifacts.bzl", "maven_fetch_remote_artifacts")

maven_fetch_remote_artifacts()

# Rust

load("@io_bazel_rules_rust//rust:repositories.bzl", "rust_repository_set")

rust_version = "1.49.0"

rustfmt_version = "1.4.20"

rust_repository_set(
    name = "rust_linux_x86_64",
    edition = "2018",
    exec_triple = "x86_64-unknown-linux-gnu",
    extra_target_triples = ["wasm32-unknown-unknown"],
    rustfmt_version = rustfmt_version,
    version = rust_version,
)

rust_repository_set(
    name = "rust_darwin_x86_64",
    edition = "2018",
    exec_triple = "x86_64-apple-darwin",
    extra_target_triples = ["wasm32-unknown-unknown"],
    rustfmt_version = rustfmt_version,
    version = rust_version,
)

load("@io_bazel_rules_rust//:workspace.bzl", "bazel_version")

bazel_version(name = "bazel_version")

load("//rules/rust:crates.bzl", "raze_fetch_remote_crates")

raze_fetch_remote_crates()

register_toolchains("//:proto-toolchain")

# NodeJS
load("@build_bazel_rules_nodejs//:index.bzl", "node_repositories", "yarn_install")

node_repositories(
    node_repositories = {
        "15.5.1-darwin_amd64": ("node-v15.5.1-darwin-x64.tar.gz", "node-v15.5.1-darwin-x64", "4507dab0481b0b5374b5758b1eba7d105c8cbcb173548119b04d9ef7d9f1d40f"),
        "15.5.1-linux_amd64": ("node-v15.5.1-linux-x64.tar.xz", "node-v15.5.1-linux-x64", "dbc41a611d99aedf2cfd3d0acc50759a6b9084c7447862e990f51958d4a7aa41"),
    },
    node_version = "15.5.1",
    package_json = ["//rules/nodejs:package.json"],
    preserve_symlinks = True,
    yarn_version = "1.22.4",
)

yarn_install(
    name = "npm",
    package_json = "//rules/nodejs:package.json",
    symlink_node_modules = True,
    use_global_yarn_cache = True,
    yarn_lock = "//rules/nodejs:yarn.lock",
)

# Packaging

load("@rules_pkg//:deps.bzl", "rules_pkg_dependencies")

rules_pkg_dependencies()

# Docker Setup

load("@io_bazel_rules_docker//repositories:repositories.bzl", container_repositories = "repositories")

container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

load("@io_bazel_rules_docker//repositories:py_repositories.bzl", "py_deps")

py_deps()

load("@io_bazel_rules_docker//java:image.bzl", java_image_repos = "repositories")
load("@io_bazel_rules_docker//python3:image.bzl", py3_image_repos = "repositories")
load("@io_bazel_rules_docker//nodejs:image.bzl", nodejs_image_repos = "repositories")
load("@io_bazel_rules_docker//rust:image.bzl", rust_image_repos = "repositories")

java_image_repos()

nodejs_image_repos()

py3_image_repos()

rust_image_repos()

# Python
register_toolchains("//rules/python:py_toolchain")

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "pip_modules",
    requirements = "//rules/python:requirements.txt",
)

# K8s

load("@io_bazel_rules_k8s//k8s:k8s.bzl", "k8s_repositories")

k8s_repositories()

load("@io_bazel_rules_k8s//k8s:k8s_go_deps.bzl", k8s_go_deps = "deps")

k8s_go_deps()

# Miscellaneous

load("//rules/misc:setup.bzl", "rules_misc_setup_internal")

rules_misc_setup_internal()

load("//rules/misc:install.bzl", "rules_misc_install_internal")

rules_misc_install_internal()

# Images Install

load("//images:install.bzl", "images_install")

images_install()

# Proto / gRPC

load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")

rules_proto_dependencies()

rules_proto_toolchains()

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")

grpc_extra_deps()
