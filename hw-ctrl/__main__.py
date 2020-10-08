from . import ad_converter, current_sensors, gpio_expander, prompt
from .i2c import I2C

import json
import sys
import time
import adafruit_ds3502

args = sys.argv

ds_3502 = adafruit_ds3502.DS3502(I2C)

sensors = {
            'KL30': current_sensors.cs_kl30,
            'KL15': current_sensors.cs_kl15,
            'HSK': current_sensors.cs_hsk
            }

values = {
            'on': True,
            'off': False
}


def configure():
    gpio_expander.setIO()

def get_voltage_current(pin):
    voltage = sensors[pin].bus_voltage
    current = sensors[pin].current
    return voltage, current

def get_temperature():
    return ad_converter.read_ad()

def set_pin(pin,value):
    if pin == 'KL30':
        gpio_expander.GPB1.value = values[value]
        gpio_expander.GPB2.value = values[value]
    elif pin == 'KL15':
        gpio_expander.GPB3.value = values[value]
    elif pin =='KLS':
        gpio_expander.GPB4.value = values[value]

def set_voltage(voltage):
    voltage = round(voltage, 1)
    note ='ok'
    while(round(current_sensors.cs_kl30.bus_voltage, 1) != voltage):
        if voltage > round(current_sensors.cs_kl30.bus_voltage, 1) and ds_3502.wiper != 0:
            ds_3502.wiper = ds_3502.wiper - 1
        elif voltage > round(current_sensors.cs_kl30.bus_voltage, 1) and ds_3502.wiper == 0:
            # print("You reached the maximum possible voltage: {}".format(round(current_sensors.cs_kl30.bus_voltage, 1)))
            note = 'max'
            break
        elif voltage < round(current_sensors.cs_kl30.bus_voltage, 1) and ds_3502.wiper != 127:
            ds_3502.wiper = ds_3502.wiper + 1
        elif voltage < round(current_sensors.cs_kl30.bus_voltage, 1) and ds_3502.wiper == 127:
            # print("You reached the minimum possible voltage: {}".format(round(current_sensors.cs_kl30.bus_voltage, 1)))
            note = 'min'
            break
        time.sleep(0.01)
    return round(current_sensors.cs_kl30.bus_voltage, 1), note
def help():
    print('''
    ===Available Options===

    To configure GPIO pins:

        sudo python3 -m hil configure

    For voltage and current values from three current sensors:

        sudo python3 -m hil currentsensor KL30
        sudo python3 -m hil currentsensor KL15
        sudo python3 -m hil currentsensor HSK

    For temperature values from four thermistor:

        sudo python3 -m hil temperature

    For the status of a specified pin:

        sudo python -m hil KL30 on
        sudo python -m hil KL30 off
        sudo python -m hil KL15 on
        sudo python -m hil KL15 off
        sudo python -m hil KLS on
        sudo python -m hil KLS off

    To change the main voltage value:

        sudo python3 -m hil setvoltage "voltage"

    To see available options:

        sudo python3 -m hil help
    ''')

if __name__ == '__main__':

    if args[1] == 'configure':
        configure()

    elif args[1] == 'temperature':
        temp1, temp2, temp3, temp4 = get_temperature()
        dict = {
                'temperature1': temp1,
                'temperature2': temp2,
                'temperature3': temp3,
                'temperature4': temp4
        }
        print(json.dumps(dict, indent=4))

    elif args[1] == 'help':
        help()

    elif args[1] == 'status':
        status()
        dict = {
                'KL30': seulav[gpio_expander.GPB2.value],
                'KL15': seulav[gpio_expander.GPB3.value],
                'KLS': seulav[gpio_expander.GPB4.value]
        }
        print(json.dumps(dict, indent=4))

    elif args[1] == 'prompt':
        prompt.main()    

    elif (args[1] == 'currentsensor') and (args[2] in ['KL30','KL15','HSK']):
        voltage, current = get_voltage_current(args[2])
        dict = {
                'voltage': round(voltage,3),
                'current': round(current,3)
        }
        print(json.dumps(dict, indent=4))

    elif args[1] == 'setvoltage':
        try:
            voltage, note = set_voltage(float(args[2]))
            dict = {
                    'voltage': voltage,
                    'note': note
            }
            print(json.dumps(dict, indent=4))
        except:
            print("Misusage of entered command")

    elif args[1] in ['KL30','KL15','KLS'] and args[2] in ['on','off']:
        set_pin(args[1],args[2])

    else:
        print("Misusage of entered command")
