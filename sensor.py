#!/usr/bin/env python3

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class Sensor:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.IN)
        self.pin = pin

    def sense(self):
        return bool(GPIO.input(self.pin))

    def watcher(clock, screen, stopper):
        while not stopper.is_set():
            if self.sense():
                clock.reset()
                screen.turn(True)
            time.sleep(0.1)
