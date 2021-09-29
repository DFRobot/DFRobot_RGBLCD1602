# -*- coding: utf-8 -*-
'''file hello_world.py
 # @brief display "hello,world!"
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

colorR = 255
colorG = 0
colorB = 0

lcd=DFRobot_RGBLCD1602(16,2)

'''
  @brief set RGB
  @param r  red   range(0-255)
  @param g  green range(0-255)
  @param b  blue  range(0-255)
'''
lcd.set_RGB(colorR, colorG, colorB)
    
# Print a message to the LCD.
'''
  @brief output data to LCD to display
  @param arg output data
'''
lcd.print_out("hello, world!")

time.sleep(1)
i = 0

while True:
  i = i+1
  # set the cursor to column 0, line 1
  # (note: line 1 is the second row, since counting begins with 0):
  '''
    @brief set cursor position
    @param col columns optional range 0-15
    @param row rows optional range 0-1，0 is the first row, 1 is the second row
  '''
  lcd.set_cursor(0, 1)
  # print the number of seconds since reset:
  lcd.print_out(i)
  time.sleep(1)

