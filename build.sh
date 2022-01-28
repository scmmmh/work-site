#!/bin/bash
git checkout -- .
git pull --ff-only
python3 -m venv .venv
source .venv/bin/activate
pip install --no-cache-dir -r requirements.txt
pelican -o output -d -s publishconf.py content
