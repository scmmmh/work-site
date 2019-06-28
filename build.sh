#!/bin/bash
export PIPENV_VENV_IN_PROJECT=1
git pull
yarn install
./node_modules/.bin/gulp
pipenv install
pipenv run pelican -o output -d -s publishconf.py content
