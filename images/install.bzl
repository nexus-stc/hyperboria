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
        digest = "sha256:c65d2b75a62135c95e2c595822af9b6f6cf0f32c11bcd4a38368d7b7c36b66f5",
        registry = "index.docker.io",
        repository = "library/ubuntu",
        tag = "20.04",
    )
