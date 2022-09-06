workspace(name = "hyperboria")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "ebdf850bfef28d923a2cc67ddca86355a449b5e4f38b0a70e584dc24e5984aa6",
    strip_prefix = "bazel-skylib-f80bc733d4b9f83d427ce3442be2e07427b2cc8d",
    urls = ["https://github.com/bazelbuild/bazel-skylib/archive/f80bc733d4b9f83d427ce3442be2e07427b2cc8d.tar.gz"],
)

http_archive(
    name = "com_github_grpc_grpc",
    sha256 = "291db3c4e030164421b89833ee761a2e6ca06b1d1f8e67953df762665d89439d",
    strip_prefix = "grpc-1.46.1",
    urls = ["https://github.com/grpc/grpc/archive/v1.46.1.tar.gz"],
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
    name = "io_bazel_rules_k8s",
    sha256 = "a08850199d6900328ef899906717fb1dfcc6cde62701c63725748b2e6ca1d5d9",
    strip_prefix = "rules_k8s-d05cbea5c56738ef02c667c10951294928a1d64a",
    urls = ["https://github.com/bazelbuild/rules_k8s/archive/d05cbea5c56738ef02c667c10951294928a1d64a.tar.gz"],
)

http_archive(
    name = "rules_pkg",
    sha256 = "b9a5bdfe4f8ce0dedf9387eadd9f4844c383118b3f4cc27b586626b7998141c3",
    strip_prefix = "rules_pkg-4b0b9f4679484f107f750a60190ff5ec6b164a5f/pkg",
    urls = ["https://github.com/bazelbuild/rules_pkg/archive/4b0b9f4679484f107f750a60190ff5ec6b164a5f.tar.gz"],
)

http_archive(
    name = "rules_proto_grpc",
    sha256 = "507e38c8d95c7efa4f3b1c0595a8e8f139c885cb41a76cab7e20e4e67ae87731",
    strip_prefix = "rules_proto_grpc-4.1.1",
    urls = ["https://github.com/rules-proto-grpc/rules_proto_grpc/archive/4.1.1.tar.gz"],
)

http_archive(
    name = "rules_python",
    sha256 = "95525d542c925bc2f4a7ac9b68449fc96ca52cfba15aa883f7193cdf745c38ff",
    strip_prefix = "rules_python-cccbfb920c8b100744c53c0c03900f1be4040fe8",
    url = "https://github.com/ppodolsky/rules_python/archive/cccbfb920c8b100744c53c0c03900f1be4040fe8.tar.gz",
)

http_archive(
    name = "org_chromium_chromium",
    build_file_content = """exports_files(["chromedriver"])""",
    strip_prefix = "ungoogled-chromium_103.0.5060.134_1.vaapi_linux",
    urls = [
        "https://github.com/macchrome/linchrome/releases/download/v103.0.5060.134-r1002911-portable-ungoogled-Lin64/ungoogled-chromium_103.0.5060.134_1.vaapi_linux.tar.xz",
    ],
)

http_archive(
    name = "org_izihawa_summa",
    sha256 = "f0cf66c9cb691adea3a1bf1fcd62d315042d606e901adaa61ec28061499426ff",
    strip_prefix = "summa-ab7ea3eba9846094d1792077d578ddb585d8e070",
    url = "https://github.com/izihawa/summa/archive/ab7ea3eba9846094d1792077d578ddb585d8e070.tar.gz",
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
load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3_10",
    python_version = "3.10",
)

load("@python3_10//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip_modules",
    python_interpreter_target = interpreter,
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

load("@com_google_googleapis//:repository_rules.bzl", "switched_rules_by_language")

switched_rules_by_language(
    name = "com_google_googleapis_imports",
    cc = True,
    grpc = True,
    python = True,
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

load("@io_bazel_rules_docker//python3:image.bzl", py3_image_repos = "repositories")
load("@io_bazel_rules_docker//nodejs:image.bzl", nodejs_image_repos = "repositories")

nodejs_image_repos()

py3_image_repos()

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
