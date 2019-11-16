#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "${DIR}/.."

if [[ ! -f .env ]]; then
    cp .env.sample .env
fi

if [[ ! -d venv ]]; then
    virtualenv venv
fi

if [[ "${VIRTUAL_ENV}" != "$(pwd)/venv" ]]; then
    . ./venv/bin/activate
fi

if [[ -f requirements.txt ]]; then
    pip install -r requirements.txt
fi

cd -
