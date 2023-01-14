# -*- coding: utf-8 -*-
''' file DFRobot_RGBLCD1602.cpp
  # DFRobot_RGBLCD1602 class infrastructure, the implementation of basic methods
  @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @licence     The MIT License (MIT)
  @maintainer [yangfeng](feng.yang@dfrobot.com)
  @version  V1.0
  @date  2021-09-24
  @url https://github.com/DFRobot/DFRobot_RGBLCD1602
'''
import time
import sys
import wiringpi

LCD_ADDRESS   =  (0x7c>>1)

#color define
WHITE      =     0
RED        =     1
GREEN      =     2
BLUE       =     3
REG_MODE1  =     0x00
REG_MODE2  =     0x01
REG_OUTPUT =     0x08
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

#flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

#flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

#flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

#flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00



class DFRobot_RGBLCD1602:
  def __init__(self, rgb_addr,col, row):
    #self.i2c=i2c
    self._row = row
    self._col = col
    self.RGB_ADDRESS = rgb_addr
    print("LCD _row=%d _col=%d"%(self._row,self._col))
    self.LCD = wiringpi.wiringPiI2CSetup(LCD_ADDRESS)
    if self.RGB_ADDRESS == 0x60:
      self.RGB = wiringpi.wiringPiI2CSetup(0x60)
      wiringpi.wiringPiI2CWriteReg8(self.RGB,REG_MODE1, 1)
      self.REG_RED    =     0x04      
      self.REG_GREEN  =     0x03
      self.REG_BLUE   =     0x02
      self.REG_ONLY   =     0x02
    elif self.RGB_ADDRESS == (0x60>>1) :
      self.RGB = wiringpi.wiringPiI2CSetup((0x60>>1))
      self.REG_RED    =     0x06
      self.REG_GREEN  =     0x07
      self.REG_BLUE   =     0x08
      self.REG_ONLY   =     0x08
    elif self.RGB_ADDRESS == (0x6B) :
      self.RGB = wiringpi.wiringPiI2CSetup(0x6B)
      self.REG_RED    =     0x06
      self.REG_GREEN  =     0x05
      self.REG_BLUE   =     0x04
      self.REG_ONLY   =     0x04
    self._show_function = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS
    self._begin(self._row,self._col)



  '''
    @brief write character
    @param data the written data
  '''
  def write(self,data):
    b=bytearray(2)
    b[0]=0x40
    b[1]=data
    wiringpi.wiringPiI2CWriteReg8(self.LCD,0x40,data)

  '''
    @brief set RGB
    @param r  red   range(0-255)
    @param g  green range(0-255)
    @param b  blue  range(0-255)
  '''
  def set_RGB(self,r,g,b):
    if self.RGB_ADDRESS == (0x60>>1):
      r=int(r*192/255)
      g=int(g*192/255)
      b=int(b*192/255)
    self._set_reg(self.REG_RED,r)
    self._set_reg(self.REG_GREEN,g)
    self._set_reg(self.REG_BLUE,b)
    if self.RGB_ADDRESS == 0x6b:
      self._set_reg(0x07,0xFF)
  '''
    @brief set cursor position
    @param col columns optional range 0-15
    @param row rows optional range 0-1，0 is the first row, 1 is the second row
  '''
  def set_cursor(self,col,row):
    if(row == 0):
      col|=0x80
    else:
      col|=0xc0
    self._command(col)

  '''
    @brief clear the display and return the cursor to the initial position (position 0)
  '''
  def clear(self):
    self._command(LCD_CLEARDISPLAY)
    time.sleep(0.002)

  '''
    @brief scroll left to display
  '''
  def scroll_display_left(self):
    self._command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT)
  '''
    @brief scroll right to display
  '''
  def scroll_display_right(self):
    self._command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT)

  '''
    @brief output data to LCD to display
    @param arg output data
  '''
  def print_out(self,arg):
    if(isinstance(arg,int)):
      arg=str(arg)

    for x in bytearray(arg,'utf-8'):
      self.write(x)

  '''
    @brief return the cursor to the initial position（0,0）
  '''
  def home(self):
    self._command(LCD_RETURNHOME)        # set cursor position to zero
    time.sleep(1)        # this _command takes a long time!

    '''
      @brief Turn off the display
    '''
  def no_display(self):
    self._show_control &= ~LCD_DISPLAYON 
    self._command(LCD_DISPLAYCONTROL | self._show_control)

  '''
    @brief Turn on the display
  '''
  def display(self):
    self._show_control |= LCD_DISPLAYON 
    self._command(LCD_DISPLAYCONTROL | self._show_control)

  '''
    @brief Turn  off the blinking showCursor
  '''
  def stop_blink(self):
    self._show_control &= ~LCD_BLINKON 
    self._command(LCD_DISPLAYCONTROL | self._show_control)

  '''
    @brief Turn on  the blinking showCursor
  '''
  def blink(self):
    self._show_control |= LCD_BLINKON 
    self._command(LCD_DISPLAYCONTROL | self._show_control)

  '''
    @brief Turn off the underline showCursor 
  '''
  def no_cursor(self):
    self._show_control &= ~LCD_CURSORON 
    self._command(LCD_DISPLAYCONTROL | self._show_control)

  '''
    @brief Turn on the underline showCursor 
  '''
  def cursor(self):
    self._show_control |= LCD_CURSORON 
    self._command(LCD_DISPLAYCONTROL | self._show_control)

  '''
    @brief This is for text that flows Left to Right
  '''
  def left_to_right(self):
    self._show_mode |= LCD_ENTRYLEFT 
    self._command(LCD_ENTRYMODESET | self._show_mode)

  '''
    @brief This is for text that flows Right to Left
  '''
  def right_to_left(self):
    self._show_mode &= ~LCD_ENTRYLEFT 
    self._command(LCD_ENTRYMODESET | self._show_mode)

  '''
    @brief This will 'left justify' text from the showCursor
  '''
  def no_autoscroll(self):
    self._show_mode &= ~LCD_ENTRYSHIFTINCREMENT 
    self._command(LCD_ENTRYMODESET | self._show_mode)

  '''
    @brief This will 'right justify' text from the showCursor
  '''
  def autoscroll(self):
    self._show_mode |= LCD_ENTRYSHIFTINCREMENT 
    self._command(LCD_ENTRYMODESET | self._show_mode)

  '''
    @brief Allows us to fill the first 8 C
    @param location substitute character range（0-7）
    @param charmap  character listing the size is 8 bytes
  '''
  def customSymbol(self,location, charmap):
    location &= 0x7  # we only have 8 locations 0-7
    self._command(LCD_SETCGRAMADDR | (location << 3))
    for i in range(0,8):
      wiringpi.wiringPiI2CWriteReg8(self.LCD,0x40,charmap[i])

  '''
    @brief set the backlight
    @param mode  true indicates the backlight is turned on and set to white, false indicates the backlight is turned off
  '''
  def setBacklight(self,mode):
    if(mode):
      self.set_color_white()      # turn backlight on
    else:
      self.close_backlight()        # turn backlight off

  '''
    @brief output string
  '''
  def printstr(self,c):
    #/< This function is not identical to the function used for "real" I2C displays
    #/< it's here so the user sketch doesn't have to be changed 
    self.print_out(c)
 
  '''
     @brief set backlight PWM output
     @param color  backlight color  Preferences：REG_RED\REG_GREEN\REG_BLUE
     @param pwm  color intensity   range(0-255)
  '''
  def set_pwm(self,color,pwm):
    self._set_reg(color, pwm)
    if self.RGB_ADDRESS == 0x6b:
      self._set_reg(0x07,0xFF)

  '''
     @brief set the backlight to white
  '''
  def set_color_white(self):
    self.set_RGB(255, 255, 255)

  '''
    @brief close the backlight
  '''
  def close_backlight(self):
    self.set_RGB(0, 0, 0)

  '''
    @brief the initialization function
    @param cols columns optional range 0-15
    @param lines rows optional range 0-1，0 is the first row, 1 is the second row
    @param dotsize  character size LCD_5x8DOTS\LCD_5x10DOTS
  '''
  def _begin(self,cols,lines,dotsize=LCD_5x8DOTS):
    if (lines > 1):
        self._show_function |= LCD_2LINE 
     
    self._num_lines = lines 
    self._curr_line = 0 

    # for some 1 line displays you can select a 10 pixel high font
    if ((dotsize != 0) and (lines == 1)) :
        self._show_function |= LCD_5x10DOTS 
     
    # SEE PAGE 45/46 FOR INITIALIZATION SPECIFICATION!
    # according to datasheet, we need at least 40ms after power rises above 2.7V
    # before sending _commands. Arduino can turn on way befer 4.5V so we'll wait 50
    #delayMicroseconds(50000);
    time.sleep(0.05)

    # this is according to the hitachi HD44780 datasheet
    # page 45 figure 23

    # Send function set _command sequence
    self._command(LCD_FUNCTIONSET | self._show_function)
    #delayMicroseconds(4500);  # wait more than 4.1ms
    time.sleep(0.005)
    # second try
    self._command(LCD_FUNCTIONSET | self._show_function)
    #delayMicroseconds(150);
    time.sleep(0.005)
    # third go
    self._command(LCD_FUNCTIONSET | self._show_function)
    # finally, set # lines, font size, etc.
    self._command(LCD_FUNCTIONSET | self._show_function)
    # turn the display on with no cursor or blinking default
    self._show_control = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF 
    self.display()
    # clear it off
    self.clear()
    # Initialize to default text direction (for romance languages)
    self._show_mode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT 
    # set the entry mode
    self._command(LCD_ENTRYMODESET | self._show_mode)
    if self.RGB_ADDRESS == 0x60:
      # backlight init
      self._set_reg(REG_MODE1, 0)
      # set LEDs controllable by both PWM and GRPPWM registers
      self._set_reg(REG_OUTPUT, 0xFF)
      # set MODE2 values
      # 0010 0000 -> 0x20  (DMBLNK to 1, ie blinky mode)
      self._set_reg(REG_MODE2, 0x20)
    elif self.RGB_ADDRESS == (0x60>>1) :
      self._set_reg(0x04, 0x15)
    elif self.RGB_ADDRESS == (0x6B) :
      self._set_reg(0x2F, 0x00)
      self._set_reg(0x00, 0x20)
      self._set_reg(0x01, 0x00)
      self._set_reg(0x02, 0x01)
      self._set_reg(0x03, 0x04)
    self.set_color_white()

  '''
    @brief send command
    @param data the sent data
  '''
  def _command(self,cmd):
    b=bytearray(2)
    b[0]=0x80
    b[1]=cmd
    wiringpi.wiringPiI2CWriteReg8(self.LCD,0x80,cmd)

  '''
    @brief set the register
    @param addr register address
    @param data data
  '''
  def _set_reg(self,reg,data):
    b=bytearray(1)
    b[0]=data
    wiringpi.wiringPiI2CWriteReg8(self.RGB,reg,data)
