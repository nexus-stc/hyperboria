"""
Install various images
"""

load("@io_bazel_rules_docker//container:pull.bzl", "container_pull")

def images_install():
    """
    Docker predefined images
    """

    container_pull(
        name = "ubuntu",
        digest = "sha256:5403064f94b617f7975a19ba4d1a1299fd584397f6ee4393d0e16744ed11aab1",
        registry = "index.docker.io",
        repository = "library/ubuntu",
        tag = "20.04",
    )
    container_pull(
        name = "jupyter",
        registry = "index.docker.io",
        repository = "jupyter/tensorflow-notebook",
        tag = "latest",
    )
