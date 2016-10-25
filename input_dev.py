#!/usr/bin/env python3

import struct

from threadable import Threadable


class InputDev(Threadable):
    def __init__(self, event_file, action=lambda: None):
        self.in_struct = struct.calcsize('llHHI')
        self.event_file = event_file
        self.action = action
        super().__init__()

    def read(self):
        return self.fh.read(self.in_struct)

    def close(self):
        self.fh.close()

    def loop(self):
        self.read()
        self.action()

    def start(self):
        self.fh = open(self.event_file, 'rb')
        super().start()

    def stop(self):
        super().stop()
        self.close()

