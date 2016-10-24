#!/usr/bin/env python3

import sys
import time

from clock import Clock
from keyboard import Keyboard
from screen import Screen

from thread_funs import make_counter, make_key_watcher

clock = Clock(0, 10, 1)
screen = Screen(True)
keyboard = Keyboard("/dev/input/event0")

counter, count_stopper = make_counter(clock, screen)
key_watcher, key_stopper = make_key_watcher(clock, screen, keyboard)

def main ():
    counter.start()
    key_watcher.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            count_stopper.set()
            key_stopper.set()
            return 0

sys.exit(main())
