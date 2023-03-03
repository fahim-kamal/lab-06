from grove_rgb_lcd import *
from grovepi import *
from rotary import RotarySensor
import time

ROTARY_PIN = 0

class data:
    def __init__(self, threshold, distance):
        self.threshold = threshold
        self.distance = distance


def getData(US_PIN, sensor: RotarySensor):
    # Get reading from rotary angle detector and ultrasonic sensor
    angle = sensor.read()
    distance_cm = ultrasonicRead(US_PIN)

    # Convert data to suitable format
    threshold_cm = round((517 / 300) * angle)

    result = data(threshold_cm, distance_cm)

    return result

def display(result: data):
    line1 = " {}cm".format(result.threshold)
    line2 = " {}cm".format(result.distance)

    if result.distance >= result.threshold:
        setRGB(255, 0, 0) # Red
        line1 = line1 + " OBJ PRES"
    else:
        setRGB(124, 242, 0) # Green
        

    line1 = line1.ljust(16)
    line2 = line2.ljust(16)

    setText(line1 + line2)


if __name__ == "__main__":
    rs = RotarySensor(ROTARY_PIN)

    res = getData(2, rs)
    display(res)

    while True:
        if(read_interrupt_state(ROTARY_PIN) == True):
            res = getData(2, rs)
            display(res)




    
