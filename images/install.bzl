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
        digest = "sha256:d0b4808a158b42b6efb3ae93abb567b1cb6ee097221813c0315390de0fa320b9",
        registry = "index.docker.io",
        repository = "library/ubuntu",
        tag = "21.10",
    )
