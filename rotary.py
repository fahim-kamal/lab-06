import time
from grovepi import *

class RotarySensor():
    def __init__(self, port):
        self.port = port
        self.ADC_REF = 5
        self.GROVE_VCC = 5
        self.FULL_ANGLE = 300
    
        pinMode(self.port, "INPUT")
        time.sleep(1)

    def read(self):
        sensor_value = analogRead(self.port)
        voltage = sensor_value * self.ADC_REF / 1023
        degrees = voltage * self.FULL_ANGLE / self.GROVE_VCC
        print(sensor_value, degrees)
        return round(degrees)

