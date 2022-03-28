workspace(
    name = "hyperboria",
    managed_directories = {"@npm": ["rules/nodejs/node_modules"]},
)

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "ebdf850bfef28d923a2cc67ddca86355a449b5e4f38b0a70e584dc24e5984aa6",
    strip_prefix = "bazel-skylib-f80bc733d4b9f83d427ce3442be2e07427b2cc8d",
    urls = [
        "https://github.com/bazelbuild/bazel-skylib/archive/f80bc733d4b9f83d427ce3442be2e07427b2cc8d.tar.gz",
    ],
)

# ToDo: wait for https://github.com/bazelbuild/rules_docker/pull/1638
http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "c2a283bea1ea30a3ceb9e5388a4c8c8eef68a815ac86f1d381f9d35cdee57f1b",
    strip_prefix = "rules_docker-46d29e34399a992087c857b13d8dcb8ec80dfd85",
    urls = [
        "https://github.com/the-superpirate/rules_docker/archive/46d29e34399a992087c857b13d8dcb8ec80dfd85.tar.gz",
    ],
)

http_archive(
    name = "build_bazel_rules_nodejs",
    sha256 = "f7037c8e295fdc921f714962aee7c496110052511e2b14076bd8e2d46bc9819c",
    urls = ["https://github.com/bazelbuild/rules_nodejs/releases/download/4.4.5/rules_nodejs-4.4.5.tar.gz"],
)

http_archive(
    name = "io_bazel_rules_k8s",
    sha256 = "a08850199d6900328ef899906717fb1dfcc6cde62701c63725748b2e6ca1d5d9",
    strip_prefix = "rules_k8s-d05cbea5c56738ef02c667c10951294928a1d64a",
    urls = [
        "https://github.com/bazelbuild/rules_k8s/archive/d05cbea5c56738ef02c667c10951294928a1d64a.tar.gz",
    ],
)

http_archive(
    name = "rules_rust",
    sha256 = "30c1b40d77a262e3f7dba6e4267fe4695b5eb1e68debc6aa06c3e09d429ae19a",
    strip_prefix = "rules_rust-0.1.0",
    urls = [
        "https://github.com/bazelbuild/rules_rust/archive/0.1.0.tar.gz",
    ],
)

http_archive(
    name = "rules_jvm_external",
    sha256 = "2a547d8d5e99703de8de54b6188ff0ed470b3bfc88e346972d1c8865e2688391",
    strip_prefix = "rules_jvm_external-3.3",
    urls = [
        "https://github.com/bazelbuild/rules_jvm_external/archive/3.3.tar.gz",
    ],
)

http_archive(
    name = "rules_pkg",
    sha256 = "b9a5bdfe4f8ce0dedf9387eadd9f4844c383118b3f4cc27b586626b7998141c3",
    strip_prefix = "rules_pkg-4b0b9f4679484f107f750a60190ff5ec6b164a5f/pkg",
    urls = [
        "https://github.com/bazelbuild/rules_pkg/archive/4b0b9f4679484f107f750a60190ff5ec6b164a5f.tar.gz",
    ],
)

http_archive(
    name = "rules_proto_grpc",
    sha256 = "507e38c8d95c7efa4f3b1c0595a8e8f139c885cb41a76cab7e20e4e67ae87731",
    strip_prefix = "rules_proto_grpc-4.1.1",
    urls = ["https://github.com/rules-proto-grpc/rules_proto_grpc/archive/4.1.1.tar.gz"],
)

http_archive(
    name = "rules_python",
    sha256 = "15f84594af9da06750ceb878abbf129241421e3abbd6e36893041188db67f2fb",
    strip_prefix = "rules_python-0.7.0",
    urls = ["https://github.com/bazelbuild/rules_python/archive/0.7.0.tar.gz"],
)

# Images Install

load("//images:install.bzl", "images_install")

images_install()

# Go

load("//rules/go:setup.bzl", "go_setup")

go_setup()

load("//rules/go:install.bzl", "go_install")

go_install()

# Python
register_toolchains("//rules/python:py_toolchain")

load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip_modules",
    requirements_lock = "//rules/python:requirements-lock.txt",
)

load("@pip_modules//:requirements.bzl", "install_deps")

install_deps()

# Proto / gRPC

load("@rules_proto_grpc//:repositories.bzl", "rules_proto_grpc_repos", "rules_proto_grpc_toolchains")

rules_proto_grpc_toolchains()

rules_proto_grpc_repos()

load("@rules_proto_grpc//js:repositories.bzl", "js_repos")

js_repos()

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")

grpc_extra_deps()

# Java

load("//rules/java:artifacts.bzl", "maven_fetch_remote_artifacts")

maven_fetch_remote_artifacts()

# Rust

load("@rules_rust//rust:repositories.bzl", "rust_repositories")

rust_repositories(
    edition = "2021",
    version = "1.59.0",
)

load("//rules/rust:crates.bzl", "raze_fetch_remote_crates")

raze_fetch_remote_crates()

# NodeJS
load("@build_bazel_rules_nodejs//:index.bzl", "node_repositories", "yarn_install")

node_repositories(
    package_json = ["//rules/nodejs:package.json"],
    preserve_symlinks = True,
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

# K8s

load("@io_bazel_rules_k8s//k8s:k8s.bzl", "k8s_defaults", "k8s_repositories")

k8s_repositories()

load("@io_bazel_rules_k8s//k8s:k8s_go_deps.bzl", k8s_go_deps = "deps")

k8s_go_deps()

k8s_defaults(
    name = "k8s_deploy",
    image_chroot = "registry.infra.svc.cluster.local",
)

# Miscellaneous

load("//rules/misc:setup.bzl", "rules_misc_setup_internal")

rules_misc_setup_internal()

load("//rules/misc:install.bzl", "rules_misc_install_internal")

rules_misc_install_internal()
