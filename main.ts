/* Copyright (c) 2023 MTHS All rights reserved
 *
 * Created by: Julianne Leblanc-Peltier
 * Created on: Sep 2023
 * This program displays the current temperature on a MicroBit
*/

let temperature = input.temperature()

basic.clearScreen()
basic.pause(1000)

input.onButtonPressed(Button.A, function () {
  temperature = input.temperature()
  basic.showString('The temperature is' + (temperature).toString())
  basic.showString('C.')
})
