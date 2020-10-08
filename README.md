# hil

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

It is important to configure GPIO pins every time RasPi turned on with the command below:

```console
    sudo python3 -m hil configure
```

## Usage

## Usage

To configure GPIO pins:

    sudo python3 -m hil configure

For voltage and current values from three current sensors:

    sudo python3 -m hil currentsensor KL30
    sudo python3 -m hil currentsensor KL15
    sudo python3 -m hil currentsensor HSK

For temperature values from four thermistor:

    sudo python3 -m hil temperature

To set a specified pin:

    sudo python -m hil KL30 on
    sudo python -m hil KL30 off
    sudo python -m hil KL15 on
    sudo python -m hil KL15 off
    sudo python -m hil KLS on
    sudo python -m hil KLS off

For status of specified pins:

    sudo python -m hil status

To change the main voltage value:

    sudo python3 -m hil setvoltage "voltage"

To see available options:

    sudo python3 -m hil help
