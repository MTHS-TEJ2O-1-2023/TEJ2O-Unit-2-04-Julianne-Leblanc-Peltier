"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *
import random

temperature = input.temperature

display.clear
sleep(1)

while True:
    if button_a.is_pressed():
        display.scroll("The temperature is:")
        display.show(str(temperature))
        display.scroll("C.")
