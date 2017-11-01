#!/bin/bash
echo "Content-Type: text/html"
echo ""
echo "<!DOCTYPE html><html><head><title>Rebuild</title></head><body><ul><li>"
hg pull --update
echo "</li><li>"
npm install
echo "</li><li>"
./node_modules/.bin/gulp --gulpfile ./theme-gulpfile.js
echo "</li><li>"
source ./venv/bin/activate
pip install -r requirements.txt
echo "</li><li>"
./venv/bin/pelican content -s publishconf.py
echo "</li></ul></body></html>"
