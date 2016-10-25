#!/usr/bin/env python3

import time
from threadable import Threadable


class CountDown(Threadable):
    def __init__(self, count, step=1, action=lambda: None):
        self.count = count
        self.step = step
        self.state = count
        self.action = action
        super().__init__()

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

    def reset(self):
        self.state = self.count

    def loop(self):
        if self.advance():
            self.action()
