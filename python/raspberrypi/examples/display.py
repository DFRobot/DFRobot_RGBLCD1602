# -*- coding: utf-8 -*-
'''file display.py
 # @brief display.
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
'''
  @brief output data to LCD to display
  @param arg output data
'''
lcd.print_out("hello world!")
while True:
  '''
    @brief Turn off the display
  '''
  lcd.no_display()
  time.sleep(0.5)
  '''
    @brief Turn on the display
  '''
  lcd.display()
  time.sleep(0.5)

