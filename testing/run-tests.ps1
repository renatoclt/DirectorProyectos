$ErrorActionPreference = "Stop"
python -m pip install -r "$PSScriptRoot/requirements.txt"
python "$PSScriptRoot/run_tests.py"
exit $LASTEXITCODE
