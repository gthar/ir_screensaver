#!/usr/bin/env python3

import RPi.GPIO as GPIO
import threading
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class Sensor:
    def __init__(self, pin, action=lambda: None):
        GPIO.setup(pin, GPIO.IN)
        self.pin = pin
        self.action = action
        self.stopper = threading.Event()

    def sense(self):
        return bool(GPIO.input(self.pin))

    def go(self):
        while not self.stopper.is_set():
            if self.sense():
                self.action()
            time.sleep(0.1)

    def start(self):
        threading.Thread(target=self.go).start()

    def stop(self):
        self.stopper.set()
