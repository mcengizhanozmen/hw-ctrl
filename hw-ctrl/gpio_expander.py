from .i2c import I2C
import adafruit.mcp23017
import digitalio

GPIO_EXP = adafruit.mcp23017.MCP23017(I2C)

GPA0 = GPIO_EXP.get_pin(0)
GPA1 = GPIO_EXP.get_pin(1)
GPA2 = GPIO_EXP.get_pin(2)
GPA3 = GPIO_EXP.get_pin(3)
GPA4 = GPIO_EXP.get_pin(4)
GPA5 = GPIO_EXP.get_pin(5)

GPB0 = GPIO_EXP.get_pin(8)
GPB1 = GPIO_EXP.get_pin(9)
GPB2 = GPIO_EXP.get_pin(10)
GPB3 = GPIO_EXP.get_pin(11)
GPB4 = GPIO_EXP.get_pin(12)


def setIO():

    GPA0.direction = digitalio.Direction.INPUT
    GPA1.direction = digitalio.Direction.INPUT
    GPA2.direction = digitalio.Direction.INPUT
    GPA3.direction = digitalio.Direction.INPUT
    GPA4.direction = digitalio.Direction.INPUT
    GPA5.direction = digitalio.Direction.INPUT

    GPB0.direction = digitalio.Direction.OUTPUT
    GPB1.direction = digitalio.Direction.OUTPUT
    GPB2.direction = digitalio.Direction.OUTPUT
    GPB3.direction = digitalio.Direction.OUTPUT
    GPB4.direction = digitalio.Direction.OUTPUT

    GPB0.value = True
    GPB1.value = False
    GPB2.value = False
    GPB3.value = False
    GPB4.value = False


def checkIO():

    print("")

    print("PIN #                    |DIR        |VALUE")

    print("="*50)

    print("GPA0 - Door Open:        {}          {}".format(
        str(GPA0.direction).split('.')[2], "HIGH" if GPA0.value else "LOW"))
    print("GPA1 - Door Close:       {}          {}".format(
        str(GPA1.direction).split('.')[2], "HIGH" if GPA1.value else "LOW"))
    print("GPA2 - Trunk Open:       {}          {}".format(
        str(GPA2.direction).split('.')[2], "HIGH" if GPA2.value else "LOW"))
    print("GPA3 - De/Mobilize:      {}          {}".format(
        str(GPA3.direction).split('.')[2], "HIGH" if GPA3.value else "LOW"))
    print("GPA4 - KLS:              {}          {}".format(
        str(GPA4.direction).split('.')[2], "HIGH" if GPA4.value else "LOW"))
    print("GPA5 - KL15:             {}          {}".format(
        str(GPA5.direction).split('.')[2], "HIGH" if GPA5.value else "LOW"))

    print("GPB0 - Main Power:       {}          {}".format(
        str(GPB0.direction).split('.')[2], "HIGH" if GPB0.value else "LOW"))
    print("GPB1 - HSK Power:        {}          {}".format(
        str(GPB1.direction).split('.')[2], "HIGH" if GPB1.value else "LOW"))
    print("GPB2 - CDIS Power:       {}          {}".format(
        str(GPB2.direction).split('.')[2], "HIGH" if GPB2.value else "LOW"))
    print("GPB3 - KL15 Power:       {}          {}".format(
        str(GPB3.direction).split('.')[2], "HIGH" if GPB3.value else "LOW"))
    print("GPB4 - KLS Power:        {}          {}".format(
        str(GPB4.direction).split('.')[2], "HIGH" if GPB4.value else "LOW"))

    print("="*50+'\n')
