#!/usr/bin/env python3

import os
import signal
import struct
import threading
import time


class Screen:
    def __init__(self, state):
        self.state = state

    def turn(self, new_state):
        if new_state and not self.state:
            self.state = True
            print("Turn screen on")
        elif not new_state and self.state:
            self.state = False
            print("Turn screen off")

    def toggle(self):
        self.turn(not selt.state)


class Clock:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.state = start

    def advance(self):
        """
        Advance time and report whether the time is finished
        """
        if self.state <= self.end:
            time.sleep(self.step)
            self.state += self.step
            print(self.state)
            return False
        else:
            return True

    def reset(self):
        self.state = self.start

    def set_to(self, n):
        self.state = n


class Keyboard:
    def __init__(self, event_file):
        self.in_struct = struct.calcsize('llHHI')
        self.fh = open(event_file, 'rb')

    def read(self):
        return self.fh.read(self.in_struct)

    def close(self):
        self.fh.close()


def countdown(clock, screen, stop_it):
    while not stop_it.is_set():
        if clock.advance():
            screen.turn(False)
            time.sleep(1)


def key_listener(clock, screen, keyboard, stop_it):
    while not stop_it.is_set() and keyboard.read():
        clock.reset()
        screen.turn(True)


my_clock = Clock(0, 10, 1)
my_screen = Screen(True)
my_keyboard = Keyboard("/dev/input/event2")

count_stopper = threading.Event()
key_stopper = threading.Event()

count = threading.Thread(target=countdown,
                         args=(my_clock, my_screen, count_stopper))
keys = threading.Thread(target=key_listener,
                        args=(my_clock, my_screen, my_keyboard, key_stopper))
count.start()
keys.start()
