#!/usr/bin/env python3

import time
import threading


class CountDown:
    def __init__(self, count, step=1, action=lambda: None):
        self.count = count
        self.step = step
        self.state = count
        self.action = action
        self.stopper = threading.Event()

    def advance(self):
        """
        Advance time and report whether the time is finished
        """
        if self.state >= 0:
            print(self.state)
            time.sleep(self.step)
            self.state -= self.step
            return False
        else:
            return True

    def set_to(self, n):
        self.state = n

    def reset(self):
        self.set_to(self.count)

    def countdown(self, stopper):
        while not stopper.is_set():
            if self.advance():
                self.action()

    def start(self):
        threading.Thread(target=self.countdown, args=(self.stopper, )).start()

    def stop(self):
        self.stopper.set()

