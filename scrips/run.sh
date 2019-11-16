#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

${DIR}/setup.sh

cd "${DIR}/.."

if [[ "${VIRTUAL_ENV}" != "$(pwd)/venv" ]]; then
    . ./venv/bin/activate
fi

flask run

cd -
