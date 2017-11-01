#!/bin/bash
hg pull --update
npm install
./node_modules/.bin/gulp --gulpfile ./theme-gulpfile.js
source ./venv/bin/activate
pip install -r requirements.txt
./venv/bin/pelican content -s publishconf.py
