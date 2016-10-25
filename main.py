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
clock = CountDown(IDLE_TIME*60, 1, lambda: screen.turn(False))

def activity():
    clock.reset()
    screen.turn(True)

procs = [InputDev(x, activity) for x in DEV_FILES]
procs.append(clock)

###############################################################################

def main ():
    for p in procs:
        p.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            for p in procs:
                p.stop()
            return 0

if __name__ == "__main__":
    sys.exit(main())

##############################################################################
