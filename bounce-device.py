#!/usr/bin/python
# 2020 Andrew Villeneuve

import sys
from time import sleep
from gpiozero import LED

relay01 = LED(17, active_high=False, initial_value=False)
relay02 = LED(27, active_high=False, initial_value=False)
relay03 = LED(22, active_high=False, initial_value=False)
atomicpi = LED(26, active_high=False, initial_value=False)

def bounce(relay):
    relay.on()
    sleep(2)
    relay.off()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Name of relay required: [relay01,relay02,relay03,atomicpi]")
        sys.exit(1)
    elif sys.argv[1] == "relay01":
        bounce(relay01)
    elif sys.argv[1] == "relay02":
        bounce(relay02)
    elif sys.argv[1] == "relay03":
        bounce(relay03)
    elif sys.argv[1] == "atomicpi":
        bounce(atomicpi)
    else:
        print("Unrecognized device")
        sys.exit(1)

