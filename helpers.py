#!/usr/bin/env python3

import time

def activity(screen, clock):
    def f():
        clock.reset()
        time.sleep(0.01)
        screen.reset()
    return f

def set_on(screen, clock):
    def f():
        clock.reset()
        time.sleep(0.01)
        screen.turn_target(True)
    return f

def set_off(screen):
    return lambda: screen.turn_target(False)

