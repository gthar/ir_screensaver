#!/usr/bin/env python3

import struct
import threading


class InputDev:
    def __init__(self, event_file, action=lambda: None):
        self.in_struct = struct.calcsize('llHHI')
        self.event_file = event_file
        self.action = action
        self.stopper = threading.Event()

    def read(self):
        return self.fh.read(self.in_struct)

    def close(self):
        self.fh.close()

    def go(self):
        while not self.stopper.is_set():
            self.read()
            self.action()

    def start(self):
        self.fh = open(self.event_file, 'rb')
        threading.Thread(target=self.go).start()

    def stop(self):
        self.stopper.set()
        self.close()

