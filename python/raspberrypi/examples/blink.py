# -*- coding: utf-8 -*-
'''file blink.py
 # @brief blink Roll.
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

lcd=DFRobot_RGBLCD1602(col= 16,row = 2)                               #create LCD object,specify col and row

'''
  @brief output data to LCD to display
  @param arg output data
'''
lcd.print_out("hello world!")
time.sleep(1)
while True:
  '''
    @brief Turn  off the blinking showCursor
  '''
  lcd.stop_blink()
  time.sleep(3)
  '''
    @brief Turn on  the blinking showCursor
  '''
  lcd.blink()
  time.sleep(3)
