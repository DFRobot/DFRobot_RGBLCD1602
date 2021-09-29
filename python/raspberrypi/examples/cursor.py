# -*- coding: utf-8 -*-
'''file cursor.py
 # @brief cursor.
 # @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 # @licence     The MIT License (MIT)
 # @maintainer [yangfeng](feng.yang@dfrobot.com)
 # @version  V1.0
 # @date  2021-09-26
 # @url https://github.com/DFRobot/DFRobot_RGBLCD1602
'''
import sys
sys.path.append('../')
import time
from DFRobot_RGBLCD1602 import *

lcd=DFRobot_RGBLCD1602(col= 16,row = 2)                               #create LCD object,specify col and row
'''
  @brief output data to LCD to display
  @param arg output data
'''
lcd.print_out("hello, world!")

while True:

  '''
    @brief Turn off the underline showCursor 
  '''
  lcd.no_cursor()
  time.sleep(0.5)
  '''
    @brief Turn on the underline showCursor 
  '''
  lcd.cursor()
  time.sleep(0.5)
