# -*- coding: utf-8 -*-
'''file automate_roll.py
 # @brief Automate Roll.
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
lcd=DFRobot_RGBLCD1602(rgb_addr=0x60,col= 16,row = 2)                               #create LCD object,specify col and row


while True:

  '''
    @brief set cursor position
    @param col columns optional range 0-15
    @param row rows optional range 0-1，0 is the first row, 1 is the second row
  '''
  lcd.set_cursor(0, 0)
  #print from 0 to 9:
  for thisChar in range(0,10):
    '''
      @brief output data to LCD to display
      @param arg output data
    '''
    lcd.print_out(thisChar)
    time.sleep(0.5)

  # set the cursor to (16,1):
  lcd.set_cursor(16,1)

  '''
    @brief This will 'right justify' text from the showCursor
  '''
  # set the show to automatically scroll:
  lcd.autoscroll()
  # print from 0 to 9:
  for thisChar in range (0,10):
    lcd.print_out(thisChar)
    time.sleep(0.5)
  '''
    @brief This will 'left justify' text from the showCursor
  '''
  # turn off automatic scrolling
  lcd.no_autoscroll()

  '''
    @brief clear the display and return the cursor to the initial position (position 0)
  '''
  lcd.clear()
