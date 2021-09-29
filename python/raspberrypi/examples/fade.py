# -*- coding: utf-8 -*-
'''file fade.py
 # @brief fade.
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

#define REG_RED         0x04        // pwm2
#define REG_GREEN       0x03        // pwm1
#define REG_BLUE        0x02        // pwm0

def breath(color):
  for i in range(0,255,1):
    lcd.set_pwm(color, i)
    time.sleep(0.005)
    
  time.sleep(0.5)
  for i in range(254,0,-1):
    lcd.set_pwm(color, i)
    time.sleep(0.005)

  time.sleep(0.5)


lcd=DFRobot_RGBLCD1602(16,2)                               #create LCD object,specify col and row
'''
  @brief output data to LCD to display
  @param arg output data
'''
lcd.print_out("fade demo")


while True:
  breath(0x04)
  breath(0x03)
  breath(0x02)
