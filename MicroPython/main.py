"""
Created by: Julianne Leblanc-Peltier
Created on: Sep 2023
This module is a Micro:bit MicroPython program
This code displays the current temperature on a MicroBit
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
