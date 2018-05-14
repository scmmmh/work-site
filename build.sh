#!/bin/bash
export PIPENV_VENV_IN_PROJECT=1
hg pull --update
npm install
./node_modules/.bin/gulp --gulpfile ./theme-gulpfile.js
pipenv install
pipenv run pelican -o output -d -s publishconf.py content
