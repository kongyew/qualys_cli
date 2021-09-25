#!/bin/bash

# set -o errexit
# set -o pipefail
# set -o nounset

SCRIPT_RELATIVE_DIR=$(dirname "${BASH_SOURCE[0]}") 
SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"
SWAGGER_API="https://gateway.qg2.apps.qualys.com/apidocs/yaml/csapi-swagger-v1.3.yaml"
GIT_USER_ID="kongyew"
GIT_REPO_ID="qualys_containersecurityapi"
RELEASE_NOTE="Integration"


function error() {
    echo "An error occured running this script."
}

trap error SIGINT

function get_arch_type() {
    if [[ $(uname -m) == "i686" ]]; then
        echo "386"
    elif [[ $(uname -m) == "x86_64" ]]; then
        echo "amd64"
    fi
}

function get_arch_base() {
    if [[ "$OSTYPE" == "linux-gnu" ]]; then
        echo "linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "darwin"
    fi
}

echo $DIR_NAME
ARCH="$(get_arch_base)_$(get_arch_type)"
CMD="swagger-codegen generate -i generate \
 -i  $SWAGGER_API -l go \
--git-user-id $GIT_USER_ID \
--git-repo-id $GIT_REPO_ID \
--release-note $RELEASE_NOTE \
--config $SCRIPT_DIR/swagger-config.json \
-o   $SCRIPT_DIR/../api"


#command -v "$CMD"

$CMD

exit 0


