#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$(dirname $SCRIPT_DIR)")"

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    apt install curl gnupg
    curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg
    mv bazel.gpg /etc/apt/trusted.gpg.d/
    echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
    apt-get update
    apt-get -y install bazel llvm make openjdk-8-jdk python3.9 python3.9-venv python3.9-dev python-dev \
     libsqlite3-dev nodejs libev-dev libev-perl python3-distutils yarn
elif [[ "$OSTYPE" == "darwin"* ]]; then
    required_packages='bazel coreutils ibazel libev libomp llvm protobuf python3.9 sqlite3'
    brew tap bazelbuild/tap
    for required_package in $required_packages; do
        if brew ls --versions $required_package > /dev/null; then
            brew upgrade $required_package
        else
            brew install $required_package
        fi
    done
elif [[ "$OSTYPE" == "cygwin" ]]; then
    exit 1;
elif [[ "$OSTYPE" == "msys" ]]; then
    exit 1;
elif [[ "$OSTYPE" == "win32" ]]; then
    exit 1;
elif [[ "$OSTYPE" == "freebsd"* ]]; then
    exit 1;
else
    exit 1;
fi

echo "Successfully installed packages"
