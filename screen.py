#!/usr/bin/env python3

class Screen:
    """
    We can turn off the screen with tvservice
    """

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
