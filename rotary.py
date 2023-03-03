import time
import grovepi

ADC_REF = 5
GROVE_VCC = 5
FULL_ANGLE = 300

def initRotarySensor(port):
    grovepi.pinMode(port, "INPUT")
    time.sleep(1)

def getDegrees(port):
    sensor_value = grovepi.analogRead(port)

    voltage = sensor_value * ADC_REF / 1023; 

    degrees = voltage * FULL_ANGLE / GROVE_VCC

    return degrees

