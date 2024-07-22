python3.10 -m venv .venv

source .venv/bin/activate
pip install --require-virtualenv --upgrade pip
pip install --no-cache --require-virtualenv --editable .

echo "Please remember to activate the environment"
