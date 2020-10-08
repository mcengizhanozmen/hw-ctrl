from hil import current_sensors, gpio_expander, ad_converter
from cmd import Cmd
import adafruit_ds3502
import time
from hil.i2c import I2C

ds_3502 = adafruit_ds3502.DS3502(I2C)

class HilPrompt(Cmd):
    prompt = '(hil) >>> '
    intro = """

    Starting HIL Test Interface...

    ##    ##   ##   ##
    ##    ##   ##   ##
    ########   ##   ##
    ##    ##   ##   ##
    ##    ##   ##   ########

    Hardware-in-Loop v0.0.2
    CarTelSol GmbH

    For list of possible commands, please type 'help'.

    """

    def do_Read_IO(self, line):
        '''\nRead direction and voltage-level values of pre-defined GPIO-pins\n'''
        gpio_expander.checkIO()

    def do_Read_CurrentSensors(self, line):
        '''\nRead the voltage levels measured by the current sensors\n'''
        current_sensors.readSensors()

    def do_Main_Power_ON(self, line):
        '''\nTurn on main power\n'''
        gpio_expander.GPB0.value = True
        print("\nMain Power : {}\n".format("ON" if gpio_expander.GPB0.value else "OFF"))

    def do_Main_Power_OFF(self, line):
        '''\nTurn off main power\n'''
        gpio_expander.GPB0.value = False
        gpio_expander.GPB1.value = False
        gpio_expander.GPB2.value = False
        gpio_expander.GPB3.value = False
        gpio_expander.GPB4.value = False
        print("\nMain Power : {}\n".format("ON" if gpio_expander.GPB0.value else "OFF"))

    def do_CDIS_Power_ON(self, line):
        '''\nTurn on CDIS power if main power is already on\n'''
        if gpio_expander.GPB0.value:
            gpio_expander.GPB2.value = True
            print("\nCDIS Power : {}\n".format("ON" if gpio_expander.GPB2.value else "OFF"))
        else:
            print("Please make sure main power is on first.")
            print("\nMain Power : {}\n".format("ON" if gpio_expander.GPB0.value else "OFF"))
            print("\nCDIS Power : {}\n".format("ON" if gpio_expander.GPB2.value else "OFF"))

    def do_CDIS_Power_OFF(self, line):
        '''\nTurn off CDIS power\n'''
        gpio_expander.GPB2.value = False
        print("\nKL15 : {}\n".format("ON" if gpio_expander.GPB2.value else "OFF"))

    def do_HSK_Power_ON(self, line):
        '''\nTurn on HSK power if main power is already on\n'''
        if gpio_expander.GPB0.value:
            gpio_expander.GPB1.value = True
            print("\nHSK Power : {}\n".format("ON" if gpio_expander.GPB1.value else "OFF"))
        else:
            print("Please make sure main power is on first.")
            print("\nMain Power : {}\n".format("ON" if gpio_expander.GPB0.value else "OFF"))
            print("\nHSK Power  : {}\n".format("ON" if gpio_expander.GPB1.value else "OFF"))

    def do_HSK_Power_OFF(self, line):
        '''\nTurn off HSK power\n'''
        gpio_expander.GPB1.value = False
        print("\nHSK Power : {}\n".format("ON" if gpio_expander.GPB1.value else "OFF"))

    def do_KL15_ON(self, line):
        '''\nTurn on KL15 if main power is already on\n'''
        if gpio_expander.GPB0.value:
            gpio_expander.GPB3.value = True
            print("\nKL15 : {}\n".format("ON" if gpio_expander.GPB3.value else "OFF"))
        else:
            print("Please make sure main power is on first.")
            print("\nMain Power : {}\n".format("ON" if gpio_expander.GPB0.value else "OFF"))
            print("\nKL15       : {}\n".format("ON" if gpio_expander.GPB3.value else "OFF"))

    def do_KL15_OFF(self, line):
        '''\nTurn off KL15 power\n'''
        gpio_expander.GPB3.value = False
        print("\nKL15 : {}\n".format("ON" if gpio_expander.GPB3.value else "OFF"))

    def do_KLS_ON(self, line):
        '''\nTurn on KLS if main power is already on\n'''
        if gpio_expander.GPB0.value:
            gpio_expander.GPB4.value = True
            print("\nKLS : {}\n".format("ON" if gpio_expander.GPB4.value else "OFF"))
        else:
            print("Please make sure main power is on first.")
            print("\nMain Power : {}\n".format("ON" if gpio_expander.GPB0.value else "OFF"))
            print("\nKLS       : {}\n".format("ON" if gpio_expander.GPB4.value else "OFF"))

    def do_KLS_OFF(self, line):
        '''\nTurn off KLS power\n'''
        gpio_expander.GPB4.value = False
        print("\nKLS : {}\n".format("ON" if gpio_expander.GPB4.value else "OFF"))

    def do_Set_Voltage(self, arg):
        '''\nSet the output voltage coming from  the voltage regulator: setVoltage <Voltage value in between 6 and 12>\n'''
        args = arg.split()
        try:
            vltg = round(float(args[0]),1)
        except:
            print("\nMisusage of Set_Voltage command, please type 'help Set_Voltage'.\n")
            return
        if ((len(args) == 1) and (6 <= round(float(args[0]),1) <= 12)):
            vltg = round(float(args[0]), 1)
            while(round(current_sensors.cs_kl30.bus_voltage, 1) != vltg):
                if vltg > round(current_sensors.cs_kl30.bus_voltage, 1) and ds_3502.wiper != 0:
                    ds_3502.wiper = ds_3502.wiper - 1
                elif vltg > round(current_sensors.cs_kl30.bus_voltage, 1) and ds_3502.wiper == 0:
                    print("You reached the maximum possible voltage: {}".format(round(current_sensors.cs_kl30.bus_voltage, 1)))
                    break
                elif vltg < round(current_sensors.cs_kl30.bus_voltage, 1) and ds_3502.wiper != 127:
                    ds_3502.wiper = ds_3502.wiper + 1
                elif vltg < round(current_sensors.cs_kl30.bus_voltage, 1) and ds_3502.wiper == 127:
                    print("You reached the minimum possible voltage: {}".format(round(current_sensors.cs_kl30.bus_voltage, 1)))
                    break
                time.sleep(0.01)
        else:
            print("\nMisusage of setVoltage command, please type 'help Set_Voltage'.\n")

    def do_Read_AD(self, line):
        '''\nRead temperature, voltage, and resistance values from AD-Converter\n'''
        ad_converter.read_ad()

    def do_set_IO(self,line):
        '''\nSet GPIO-Expander pins to default\n'''
        gpio_expander.setIO()

    def do_Set_Currentsensor_Precision(self, arg):
        '''
        \nSet the precision of the current sensor
        For high precision enter 'Set_Currentsensor_Precision H'
        For standard precision enter 'Set_Currentsensor_Precision S'\n
        '''
        args = arg.split()
        try:
            current_sensors.precision_calibration(args[0])
        except:
            print("\nPrecision change failed.\n")

    def do_exit(self, inp):
        '''\nExit test interface\n'''
        print("\nSuccesfully exiting HIL...\n")
        return True

def main():
    HilPrompt().cmdloop()
