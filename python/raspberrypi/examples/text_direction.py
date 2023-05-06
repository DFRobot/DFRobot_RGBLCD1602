# -*- coding: utf-8 -*-
'''file text_direction.py.py
 # @brief  text direction.
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
thisChar = 'a'

'''
  @brief Turn on the underline showCursor 
'''
lcd.cursor()

while True:
  # reverse directions at 'm':
  if ((thisChar) == 'm'):
    # go right for the next letter
    '''
      @brief This is for text that flows Right to Left
    '''
    lcd.right_to_left()
  
  # reverse again at 's':
  if ((thisChar) == 's'):
    # go left for the next letter
    '''
      @brief This is for text that flows Left to Right
    '''
    lcd.left_to_right()
  
  # reset at 'z':
  if ((thisChar) > 'z'):
    '''
      @brief return the cursor to the initial position（0,0）
    '''
    lcd.home()
    # start again at 0
    thisChar = 'a'

  '''
    @brief write character
    @param data the written data
  '''
  lcd.write(ord(thisChar))
  # wait a second:
  time.sleep(0.5)
  # increment the letter:
  thisChar = chr(ord(thisChar) +1)

