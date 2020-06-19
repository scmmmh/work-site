#!/bin/bash
export PIPENV_VENV_IN_PROJECT=1
git pull
yarn install
./node_modules/.bin/gulp
poetry install
poetry run pelican -o output -d -s publishconf.py content
