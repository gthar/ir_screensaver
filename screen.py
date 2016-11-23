#!/usr/bin/env python3

import os

class Screen:
    """
    We can turn off the screen with tvservice
    """

    def __init__(self, state):
        self.state = state

    def turn(self, new_state):

        if new_state and not self.state:
            self.state = True
            os.system("/home/rilla/bin/screen_on")

        elif not new_state and self.state:
            self.state = False
            os.system("/home/rilla/bin/screen_off")

    def toggle(self):
        self.turn(not selt.state)
