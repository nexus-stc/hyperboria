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
        digest = "sha256:c27987afd3fd8234bcf7a81e46cf86c2c4c10ef06e80f0869c22c6ff22b29f9d",
        registry = "index.docker.io",
        repository = "library/ubuntu",
        tag = "22.04",
    )
