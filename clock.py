#!/usr/bin/env python3

import time


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
