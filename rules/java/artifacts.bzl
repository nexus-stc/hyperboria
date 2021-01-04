"""
Java dependencies
"""

load("@rules_jvm_external//:defs.bzl", "maven_install")

def maven_fetch_remote_artifacts():
    """
    Fetch maven artifacts
    """
    maven_install(
        artifacts = [
            "com.fasterxml.jackson.core:jackson-core:2.11.2",
            "com.fasterxml.jackson.core:jackson-databind:2.11.2",
            "org.apache.pdfbox:pdfbox:2.0.20",
            "org.apache.kafka:kafka_2.13:2.6.0",
            "org.apache.kafka:kafka-clients:2.6.0",
            "org.grobid:grobid-core:0.6.1",
            "org.yaml:snakeyaml:1.26",
        ],
        repositories = [
            "https://maven.google.com",
            "https://repo1.maven.org/maven2",
            "https://dl.bintray.com/rookies/maven",
        ],
    )
