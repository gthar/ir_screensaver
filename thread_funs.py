#!/usr/bin/env python3

import threading
import time

###############################################################################

def countdown(clock, screen, stop_it):
    while not stop_it.is_set():
        if clock.advance():
            screen.turn(False)
            time.sleep(1)


def make_counter(clock, screen):
    stopper = threading.Event()
    thread = threading.Thread(target=countdown,
                              args=(clock,
                                    screen,
                                    stopper))
    return thread, stopper

###############################################################################

def in_dev_listener(clock, screen, in_dev, stop_it):
    while not stop_it.is_set() and in_dev.read():
        clock.reset()
        screen.turn(True)


def make_dev_watchers(clock, screen, devs):
    stopper = threading.Event()
    threads = [threading.Thread(target=in_dev_listener,
                                args=(clock, screen, dev, stopper))
               for dev in devs]
    return threads, stopper

###############################################################################
