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

def key_listener(clock, screen, keyboard, stop_it):
    while not stop_it.is_set() and keyboard.read():
        clock.reset()
        screen.turn(True)


def make_key_watcher(clock, screen, keyboard):
    stopper = threading.Event()
    thread = threading.Thread(target=key_listener,
                              args=(clock,
                                    screen,
                                    keyboard,
                                    stopper))
    return thread, stopper

###############################################################################
