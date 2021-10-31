#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo 'please run me as root :)'
    return 1
fi

INSTALLED_DEPS=0
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "Executing from ${DIR}"

function verify_dependencies {
    # pre-requisites
    if [[ ! $(which scons) ]];then
        apt install scons
    else
        echo '[scons] already installed'
    fi
    if [[ ! $(which swig) ]];then
        apt install swig
    else
        echo '[swig] already installed'
    fi
    if [[ ! $(which pip) ]];then
        apt install python-pip
        pip install --upgrade pip
    else
        echo '[pip] already installed'
    fi

    if [[ ! $(which virtualenv) ]];then
        pip install virtualenv
    else
        echo '[virtualenv] already installed'
    fi
}

function ws2812_build_c {
    pushd $DIR/rpi_ws281x > /dev/null
    echo -e '\nBuild C library\n'
    scons
    popd > /dev/null
}

function ws2812_build_python {
    pushd $DIR/rpi_ws281x/python > /dev/null
    echo -e '\nBuild Python library\n'
    virtualenv examples/
    . examples/bin/activate
    python setup.py install
    INSTALLED_DEPS=1
    popd > /dev/null
}

function ws2812_build_and_install_package {
    ws2812_build_c
    ws2812_build_python
}

function ws2812_open_samples {
    if [ $INSTALLED_DEPS -eq 0 ];then
        verify_dependencies
        ws2812_build_and_install_package
    fi
    cd $DIR/rpi_ws281x/python/examples
}
