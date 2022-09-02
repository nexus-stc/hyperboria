#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$(dirname $SCRIPT_DIR)")"

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    apt install wget
    wget https://github.com/bazelbuild/bazelisk/releases/download/v1.11.0/bazelisk-linux-amd64 -O /usr/bin/bazel
    chmod +x /usr/bin/bazel
    apt-get update
    apt-get -y install llvm make python3.10 python3.10-venv python3.10-dev python-dev \
     libsqlite3-dev nodejs libev-dev libev-perl python3-distutils wireguard yarn
elif [[ "$OSTYPE" == "darwin"* ]]; then
    required_packages='bazel coreutils ibazel libev libomp llvm protobuf python3.10 sqlite3'
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
