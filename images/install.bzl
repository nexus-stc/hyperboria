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
        digest = "sha256:45ff0162921e61c004010a67db1bee7d039a677bed0cb294e61f2b47346d42b3",
        registry = "index.docker.io",
        repository = "library/ubuntu",
        tag = "20.10",
    )
