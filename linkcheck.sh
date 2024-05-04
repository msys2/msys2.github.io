#!/bin/bash

set -e
DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "${DIR}"

# touch for permissions
touch .lycheecache
docker run --init -it --rm -w /website -v $(pwd):/website lycheeverse/lychee .
