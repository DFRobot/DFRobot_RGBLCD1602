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
'''
  @brief output data to LCD to display
  @param arg output data
'''
lcd.print_out("fade demo")


while True:
  breath(lcd.REG_RED)
  breath(lcd.REG_GREEN)
  breath(lcd.REG_BLUE)
  #breath(lcd.REG_ONLY) # Monochrome use
