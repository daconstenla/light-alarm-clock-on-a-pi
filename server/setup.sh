#!/bin/bash -aeu

export PYTHON_BIN=python3
export PYTHON_PIP_BIN=pip3
export PATH=/usr/local/opt/python@3.10/Frameworks/Python.framework/Versions/3.10/bin:${PATH}

# override default's python version
alias python=${PYTHON_BIN}
# ensure deps are installed

function check_deps_and_install {
    $PYTHON_PIP_BIN install -r requirements.txt
}

# configure the virtualenv
virtualenv pythonenv
source ./pythonenv/bin/activate

# execute the server now :)
FLASK_APP=app.py
FLASK_ENV=development

flask run
