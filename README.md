# hw-ctrl

A Python package for controlling the hardware of Hardware-in-Loop

## Installation

First, one needs to clone into the [hil-repository](https://git.cartelsol.info/minicate/hil-py).

```console
$ git clone git@git.cartelsol.info:minicate/hil-py.git
$ cd hil-py
```

Make sure that python3 and pip3 are already installed.

```console
$ python3 --version
Python 3.x.x
$ pip3 --version
pip x.x.x from /usr/lib/python3/... (python 3.x)
```

When pip3 is currently not installed, please install it before you continue with the next steps.

```console
$ sudo apt-get install python3-pip
```

After going into hil-py/ directory:

```console
$ sudo python3 setup.py install
$ sudo pip3 install -r requirements.txt
```

Command above will install hil as a Python package. Please check installed packages with:

```console
$ pip3 freeze
```

You need to see that hil has been installed.

```console
hil==0.0.2
```

To make sure that certain libraries are installed correctly, please run the command below. Sometimes we have problems with Adafruit libraries and also with numpy.

```console
$ sudo apt-get install libatlas-base-dev && sudo pip3 install numpy && sudo pip3 install adafruit-circuitpython-mcp230xx && sudo pip3 install adafruit-circuitpython-ds3502 && sudo pip3 install adafruit-circuitpython-ina219
```

## Usage

To start the testing environment:

```console
$ sudo python3 -m hil
```

To check the commands available:

```console
(hil) >>> help

Documented commands (type help <topic>):
========================================
```

You can check the functionality of these commands by writing 'help command'.
