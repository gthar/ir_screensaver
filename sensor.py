#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

from threadable import Threadable

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class Sensor(Threadable):
    def __init__(self, pin, action=lambda: None):
        GPIO.setup(pin, GPIO.IN)
        self.pin = pin
        self.action = action
        super().__init__()

    def sense(self):
        return bool(GPIO.input(self.pin))

    def loop(self):
        if self.sense():
            self.action()
        time.sleep(0.1)
