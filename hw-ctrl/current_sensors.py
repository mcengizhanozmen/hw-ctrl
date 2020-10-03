from hil.i2c import I2C
import adafruit_ina219

cs_kl30 = adafruit_ina219.INA219(I2C, 0x40)
cs_kl15 = adafruit_ina219.INA219(I2C, 0x41)
cs_hsk = adafruit_ina219.INA219(I2C, 0x44)

def readSensors():
    print("")
    print("First Current Sensor: (KL30)")
    print("============================")
    print("PSU Voltage:     {:6.3f} V".format(cs_kl30.bus_voltage + cs_kl30.shunt_voltage))
    print("Load Voltage:    {:6.3f} V".format(cs_kl30.bus_voltage))
    print("Shunt Voltage:   {:9.6f} mV".format(cs_kl30.shunt_voltage * 1000))
    print("Current:         {:9.6f} mA".format(cs_kl30.current))
    print("=============================")
    print("")
    print("Second Current Sensor: (KL15)")
    print("=============================")
    print("PSU Voltage:     {:6.3f} V".format(cs_kl15.bus_voltage + cs_kl15.shunt_voltage))
    print("Load Voltage:    {:6.3f} V".format(cs_kl15.bus_voltage))
    print("Shunt Voltage:   {:9.6f} mV".format(cs_kl15.shunt_voltage * 1000))
    print("Current:         {:9.6f} mA".format(cs_kl15.current))
    print("=============================")
    print("")
    print("Third Current Sensor: (HSK)")
    print("=============================")
    print("PSU Voltage:     {:6.3f} V".format(cs_hsk.bus_voltage + cs_hsk.shunt_voltage))
    print("Load Voltage:    {:6.3f} V".format(cs_hsk.bus_voltage))
    print("Shunt Voltage:   {:9.6f} mV".format(cs_hsk.shunt_voltage * 1000))
    print("Current:         {:9.6f} mA".format(cs_hsk.current))
    print("=============================")
    print("")

def precision_calibration(choice='S'):
    if choice=='H':
        try:
            cs_kl30.set_calibration_16V_400mA()
            cs_kl15.set_calibration_16V_400mA()
            cs_hsk.set_calibration_16V_400mA()
        except:
            print("\nCalibration change failed.\n")
    elif choice=='S':
        try:
            cs_kl30.set_calibration_32V_2A()
            cs_kl15.set_calibration_32V_2A()
            cs_hsk.set_calibration_32V_2A()
        except:
            print("\nCalibration change failed.\n")
    else:
        print("\nMisusage of precision_calibration function, use 'S' or 'H' as arguement.\n")