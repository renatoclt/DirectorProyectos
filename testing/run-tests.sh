#!/usr/bin/env sh
set -eu
python -m pip install -r "$(dirname "$0")/requirements.txt"
python "$(dirname "$0")/run_tests.py"
