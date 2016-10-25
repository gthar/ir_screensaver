#!/usr/bin/env python3

import struct


class InputDev:
    def __init__(self, event_file):
        self.in_struct = struct.calcsize('llHHI')
        self.fh = open(event_file, 'rb')

    def read(self):
        return self.fh.read(self.in_struct)

    def close(self):
        self.fh.close()
