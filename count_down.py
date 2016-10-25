#!/usr/bin/env python3

import time


class CountDown:
    def __init__(self, count, step):
        self.count = count
        self.step = step
        self.state = count

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
