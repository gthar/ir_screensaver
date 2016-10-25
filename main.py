#!/usr/bin/env python3

###############################################################################

DEV_FILES = ["/dev/input/event0",
             "/dev/input/event8",
             "/dev/input/event12"]

IDLE_TIME = 0.1  # minutes

###############################################################################

import sys
import time

from count_down import CountDown
from input_dev import InputDev
from screen import Screen

###############################################################################

screen = Screen(True)

def iddle():
    screen.turn(False)

clock = CountDown(IDLE_TIME*60, 1, iddle)

def activity():
    clock.reset()
    screen.turn(True)

devs = [InputDev(x, activity) for x in DEV_FILES]

###############################################################################

def main ():
    clock.start()
    for d in devs:
        d.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            clock.stop()
            for d in devs:
                d.stop()
            return 0

sys.exit(main())

##############################################################################
