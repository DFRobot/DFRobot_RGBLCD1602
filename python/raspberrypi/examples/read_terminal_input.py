# -*- coding: utf-8 -*-
'''file read_terminal_input.py
 # @brief  read the terminal input and display it to the LCD
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

lcd=DFRobot_RGBLCD1602(16,2)                               #create LCD object,specify col and row

while True:
  data = raw_input()
  '''
    @brief clear the display and return the cursor to the initial position (position 0)
  '''
  lcd.clear()
  '''
    @brief set cursor position
    @param col columns optional range 0-15
    @param row rows optional range 0-1，0 is the first row, 1 is the second row
  '''
  lcd.set_cursor(0,0)
  length = len(data)
  if length < 17:
    '''
      @brief output data to LCD to display
      @param arg output data
    '''
    lcd.print_out(data)
  elif length >16:
    lcd.print_out(data[:16])
    lcd.set_cursor(0,1)
    lcd.print_out(data[16:])
