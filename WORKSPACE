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
    sha256 = "5aa15ff7a83f8de8ff0346bd8274fb82eec52c947106a066dc190c2624ec1cb4",
    strip_prefix = "rules_docker-aefbc69e5f758403d50f789eee55b30a3d947418",
    urls = [
        "https://github.com/the-superpirate/rules_docker/archive/aefbc69e5f758403d50f789eee55b30a3d947418.tar.gz",
    ],
)

http_archive(
    name = "build_bazel_rules_nodejs",
    sha256 = "dd7ea7efda7655c218ca707f55c3e1b9c68055a70c31a98f264b3445bc8f4cb1",
    urls = [
        "https://github.com/bazelbuild/rules_nodejs/releases/download/3.2.3/rules_nodejs-3.2.3.tar.gz",
    ],
)

http_archive(
    name = "io_bazel_rules_k8s",
    sha256 = "c1c5a692ec994e99e9e7e77ae693086074d6dedfe72e6930efbcc66d30264032",
    strip_prefix = "rules_k8s-f1c6399cdd691b7aca90073398e8f690ec8992c6",
    urls = [
        "https://github.com/bazelbuild/rules_k8s/archive/f1c6399cdd691b7aca90073398e8f690ec8992c6.tar.gz",
    ],
)

http_archive(
    name = "rules_rust",
    sha256 = "d10dd5581f66ee169071ee06d52c52c8c7ca7467ac6266e301c0820d289b0f0b",
    strip_prefix = "rules_rust-336e1934b07211fb8736c19749919ef94df4df68",
    urls = [
        "https://github.com/bazelbuild/rules_rust/archive/336e1934b07211fb8736c19749919ef94df4df68.tar.gz",
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
    name = "rules_proto",
    sha256 = "aa1ee19226f707d44bee44c720915199c20c84a23318bb0597ed4e5c873ccbd5",
    strip_prefix = "rules_proto-40298556293ae502c66579620a7ce867d5f57311",
    urls = [
        "https://github.com/bazelbuild/rules_proto/archive/40298556293ae502c66579620a7ce867d5f57311.tar.gz",
    ],
)

_configure_python_based_on_os = """
if [[ "$OSTYPE" == "darwin"* ]]; then
    ./configure --prefix=$(pwd)/bazel_install --with-openssl=$(brew --prefix openssl)
else
    ./configure --prefix=$(pwd)/bazel_install
fi
"""

http_archive(
    name = "python_interpreter",
    build_file_content = """
exports_files(["python_bin"])
filegroup(
    name = "files",
    srcs = glob(["bazel_install/**"], exclude = ["**/* *"]),
    visibility = ["//visibility:public"],
)
""",
    patch_cmds = [
        "mkdir $(pwd)/bazel_install",
        _configure_python_based_on_os,
        "make",
        "make install",
        "ln -s bazel_install/bin/python3 python_bin",
    ],
    sha256 = "4b0e6644a76f8df864ae24ac500a51bbf68bd098f6a173e27d3b61cdca9aa134",
    strip_prefix = "Python-3.9.4",
    urls = ["https://www.python.org/ftp/python/3.9.4/Python-3.9.4.tar.xz"],
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
    strip_prefix = "subpar-9fae6b63cfeace2e0fb93c9c1ebdc28d3991b16f",
    urls = [
        "https://github.com/google/subpar/archive/9fae6b63cfeace2e0fb93c9c1ebdc28d3991b16f.tar.gz",
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

load("@rules_rust//rust:repositories.bzl", "rust_repository_set")

rust_version = "1.51.0"

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

load("//rules/rust:crates.bzl", "raze_fetch_remote_crates")

raze_fetch_remote_crates()

register_toolchains("//:proto-toolchain")

# NodeJS
load("@build_bazel_rules_nodejs//:index.bzl", "node_repositories", "yarn_install")

node_repositories(
    node_repositories = {
        "15.5.1-darwin_amd64": ("node-v15.5.1-darwin-x64.tar.gz", "node-v15.5.1-darwin-x64", "4507dab0481b0b5374b5758b1eba7d105c8cbcb173548119b04d9ef7d9f1d40f"),
        "15.5.1-linux_amd64": ("node-v15.5.1-linux-x64.tar.xz", "node-v15.5.1-linux-x64", "dbc41a611d99aedf2cfd3d0acc50759a6b9084c7447862e990f51958d4a7aa41"),
        "15.5.1-windows_amd64": ("node-v15.5.1-win-x64.zip", "node-v15.5.1-win-x64", "e1f826f9647fc7058b48c669991956a427fe4b6ccefa415a18b41715483f958d"),
        "15.5.1-linux_s390x": ("node-v15.5.1-linux-s390x.tar.gz", "node-v15.5.1-linux-s390x", "e05f949ea11e2aafc08a7972c0f41a11a3628762e857d44965e0605d3bcd143f"),
        "15.5.1-linux_arm64": ("node-v15.5.1-linux-arm64.tar.gz", "node-v15.5.1-linux-arm64", "a2d14db86c6f8a070f227940ea44a3409966f6bed14df0ec6f676fe2e2f601c9"),
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
register_toolchains("//rules/python:py_3_toolchain")

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "pip_modules",
    python_interpreter_target = "@python_interpreter//:python_bin",
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
