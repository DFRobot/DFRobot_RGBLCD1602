# -*- coding: utf-8 -*-
'''file roll.py
 # @brief  Roll show 'hello, world!'.
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

# Print a message to the LCD.
'''
  @brief output data to LCD to display
  @param arg output data
'''
lcd.print_out("hello, world!")
time.sleep(1)


while True:
  # scroll 13 positions (string length) to the left
  # to move it offscreen left:
  for positionCounter in range (0,13):
    # scroll one position left:
    '''
      @brief scroll left to display
    '''
    lcd.scroll_display_left()
    # wait a bit:
    time.sleep(0.15)

  # scroll 29 positions (string length + show length) to the right
  # to move it offscreen right:
  for positionCounter in range (0,29):
    # scroll one position right:
    '''
      @brief scroll right to display
    '''
    lcd.scroll_display_right()
    # wait a bit:
    time.sleep(0.15)

  # scroll 16 positions (show length + string length) to the left
  # to move it back to center:
  for positionCounter in range(0,16):
    # scroll one position left:
    lcd.scroll_display_left()
    # wait a bit:
    time.sleep(0.15)
    

    # delay at the end of the full loop:
  time.sleep(1)


