# -*- coding: utf-8 -*-
'''file custom_symbol.py
 # @brief Custom Symbol.
 # @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 # @licence     The MIT License (MIT)
 # @maintainer [yangfeng](feng.yang@dfrobot.com)
 # @version  V1.0
 # @date  2021-09-26
 # @url https://github.com/DFRobot/DFRobot_RGBLCD1602
'''
import sys
sys.path.append('../')
from DFRobot_RGBLCD1602 import *
import time

def _map(x,inMin,inMax,outMin,outMax):
  return (x-inMin)*(outMax-outMin)/(inMax-inMin)+outMin


# make some custom characters:
heart = [
  0b00000,
  0b01010,
  0b11111,
  0b11111,
  0b11111,
  0b01110,
  0b00100,
  0b00000
]

smiley = [
  0b00000,
  0b00000,
  0b01010,
  0b00000,
  0b00000,
  0b10001,
  0b01110,
  0b00000
]

frownie = [
  0b00000,
  0b00000,
  0b01010,
  0b00000,
  0b00000,
  0b00000,
  0b01110,
  0b10001
]

armsDown = [
  0b00100,
  0b01010,
  0b00100,
  0b00100,
  0b01110,
  0b10101,
  0b00100,
  0b01010
]

armsUp = [
  0b00100,
  0b01010,
  0b00100,
  0b10101,
  0b01110,
  0b00100,
  0b00100,
  0b01010
]
# Change the rgb_addr value based on the hardware version
# -----------------------------------------
#        Moudule        | Version|rgb_addr|
# -----------------------------------------
#   LCD1602 Module      |  V1.0  | 0x60   |
# -----------------------------------------
#   LCD1602 Module      |  V1.1  | 0x6B   |
# -----------------------------------------
#   LCD1602 RGB Module  |  V1.0  | 0x60   |
# -----------------------------------------
#   LCD1602 RGB Module  |  V1.1  | 0x2D   |
# -----------------------------------------
lcd=DFRobot_RGBLCD1602(rgb_addr=0x60,col= 16,row = 2)                               #create LCD object,specify col and row
# create a new character
'''
  @brief Allows us to fill the first 8 C
  @param location substitute character range（0-7）
  @param charmap  character listing the size is 8 bytes
'''
lcd.custom_symbol(0, heart)
lcd.custom_symbol(1, smiley)
lcd.custom_symbol(2, frownie)
lcd.custom_symbol(3, armsDown)
lcd.custom_symbol(4, armsUp)
#set up the lcd's number of columns and rows:

'''
  @brief set cursor position
  @param col columns optional range 0-15
  @param row rows optional range 0-1，0 is the first row, 1 is the second row
'''
lcd.set_cursor(0, 0)

'''
  @brief output data to LCD to display
  @param arg output data
'''
# Print a message to the lcd.
lcd.print_out("I ")
lcd.write(0)
lcd.print_out(" raspberry ")
lcd.write(1)
while True:
  lcd.set_cursor(4, 1)
  lcd.write(3)
  time.sleep(0.5)
  lcd.set_cursor(4, 1)
  lcd.write(4)
  time.sleep(0.5)
