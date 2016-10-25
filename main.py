#!/usr/bin/env python3

###############################################################################

input_devs = ["/dev/input/event0",
              "/dev/input/event8",
              "/dev/input/event12"]

KEYBOARD_DEV = "/dev/input/event0"
IDLE_TIME = 0.1  # minutes

###############################################################################

import sys
import time

from count_down import CountDown
from input_dev import InputDev
from screen import Screen

from thread_funs import make_counter, make_dev_watchers

###############################################################################

clock = CountDown(IDLE_TIME*60, 1)
screen = Screen(True)
devs = [InputDev(x) for x in input_devs]

counter, count_stopper = make_counter(clock, screen)
dev_watchers, dev_stopper = make_dev_watchers(clock, screen, devs)

###############################################################################

def main ():
    counter.start()
    for d in dev_watchers:
        d.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            count_stopper.set()
            dev_stopper.set()
            return 0

sys.exit(main())

###############################################################################
