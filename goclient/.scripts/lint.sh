#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

function error() {
    echo "An error occured while running golangci-lint."

}

trap error SIGINT

golangci-lint run