# -*- coding: utf-8 -*-
'''file set_cursor.py
 # @brief  set cursor.
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

numRows = 2
numCols = 16
'''
  @brief set RGB
  @param r  red   range(0-255)
  @param g  green range(0-255)
  @param b  blue  range(0-255)
  
'''
lcd.set_RGB(0,100,0)
while True:
  # loop from ASCII 'a' to ASCII 'z':
  for thisLetter in range(ord('a'),ord('z')):
    #lcd.clear()
    # loop over the columns:
    for thisRow in range(0,numRows):
      # loop over the rows:
      for thisCol in range(0,numCols):
        # set the cursor position:
        '''
          @brief set cursor position
          @param col columns optional range 0-15
          @param row rows optional range 0-1，0 is the first row, 1 is the second row
        '''
        lcd.set_cursor(thisCol,thisRow)
        # print the letter:
        '''
          @brief write character
          @param data the written data
        '''
        lcd.write(thisLetter)
        time.sleep(0.2)
