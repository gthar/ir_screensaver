#!/usr/bin/env python3

import glob
import yaml

from count_down import CountDown
from input_dev import InputDev
from screen import Screen
from sensor import Sensor
from socket_handler import SocketHandler


def read_config(f):
    with open(f) as fh:
        config = yaml.load(fh)
    return config


def activity(screen, clock):
    def f():
        clock.reset()
        screen.reset()
    return f

def iddle(screen):
    return lambda: screen.turn(False)


def set_on(screen, clock):
    def f():
        clock.reset()
        screen.turn_target(True)
    return f


def set_off(screen):
    return lambda: screen.turn_target(False)


def init_procs(config):
    dev_pattern = "/dev/input/event*"

    screen = Screen(state=True, target_state=config["default state"])

    iddle_seconds = config["idle time"] * 60
    clock = CountDown(iddle_seconds, 1, iddle(screen))

    # input_devs = [InputDev(x, activity(screen, clock))
                  # for x in glob.glob(dev_pattern)]

    sensor = Sensor(config["sensor pin"], activity(screen, clock))

    socket_handler = SocketHandler(wake    = activity(screen, clock),
                                   set_on  = set_on(screen, clock),
                                   set_off = set_off(screen),
                                   port    = config["port"],
                                   host    = config["host"])

    return [clock, sensor, socket_handler]
