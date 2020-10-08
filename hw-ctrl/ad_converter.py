from hil.i2c import I2C
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from numpy import log as ln

ads = ADS.ADS1115(I2C)

chan1 = AnalogIn(ads, ADS.P0)
chan2 = AnalogIn(ads, ADS.P1)
chan3 = AnalogIn(ads, ADS.P2)
chan4 = AnalogIn(ads, ADS.P3)

A = 0.8272069482 * (10**(-3))
B = 2.087897328 * (10**(-4))
C = 0.8062131944 * (10**(-7))

def read_ad():

	volt1 = chan1.voltage
	volt2 = chan2.voltage
	volt3 = chan3.voltage
	volt4 = chan4.voltage

	'''
	print("")
	print("Voltage Values")
	print("============================")
	print("1.:     {:6.3f} V".format(volt1))
	print("2.:     {:6.3f} V".format(volt2))
	print("3.:     {:6.3f} V".format(volt3))
	print("4.:     {:6.3f} V".format(volt4))
	print("=============================")
	print("")
	'''

	r1 = (volt1 * 100) / (3.3 - volt1)
	r2 = (volt2 * 100) / (3.3 - volt2)
	r3 = (volt3 * 100) / (3.3 - volt3)
	r4 = (volt4 * 100) / (3.3 - volt4)

	'''
	print("")
	print("Resistance Values")
	print("============================")
	print("1.:     {:6.3f} kOhm".format(r1))
	print("2.:     {:6.3f} kOhm".format(r2))
	print("3.:     {:6.3f} kOhm".format(r3))
	print("4.:     {:6.3f} kOhm".format(r4))
	print("=============================")
	print("")
	'''

	temp1 = (1 / (A + B * ln(r1*1000) + C * (ln(r1*1000) ** 3))) - 273.15
	temp2 = (1 / (A + B * ln(r2*1000) + C * (ln(r2*1000) ** 3))) - 273.15
	temp3 = (1 / (A + B * ln(r3*1000) + C * (ln(r3*1000) ** 3))) - 273.15
	temp4 = (1 / (A + B * ln(r4*1000) + C * (ln(r4*1000) ** 3))) - 273.15

	'''
	print("")
	print("Temperature Values")
	print("============================")
	print("1.:     {:6.1f} °C".format(temp1))
	print("2.:     {:6.1f} °C".format(temp2))
	print("3.:     {:6.1f} °C".format(temp3))
	print("4.:     {:6.1f} °C".format(temp4))
	print("=============================")
	print("")
	'''
	
	return round(temp1,1), round(temp2,1), round(temp3,1), round(temp4,1)
