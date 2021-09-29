/*!
 * @file DFRobot_RGBLCD1602.h
 * @brief DFRobot_RGBLCD1602 class infrastructure
 * @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @licence     The MIT License (MIT)
 * @maintainer [yangfeng](feng.yang@dfrobot.com)
 * @version  V1.0
 * @date  2021-09-24
 * @url https://github.com/DFRobot/DFRobot_RGBLCD1602
 */

#ifndef __DFRobot_RGBLCD1602_H__
#define __DFRobot_RGBLCD1602_H__
#include<Arduino.h>
#include <Wire.h>
#include <inttypes.h>
#include "Print.h"
#include <stdio.h>
#include <string.h>

/*!
 *  @brief Device I2C Arress
 */
#define LCD_ADDRESS     (0x7c>>1)
#define RGB_ADDRESS     (0xc0>>1)

/*!
 *  @brief color define
 */ 
#define WHITE           0
#define RED             1
#define GREEN           2
#define BLUE            3

#define REG_RED         0x04        // pwm2
#define REG_GREEN       0x03        // pwm1
#define REG_BLUE        0x02        // pwm0

#define REG_MODE1       0x00
#define REG_MODE2       0x01
#define REG_OUTPUT      0x08

/*!
 *  @brief commands
 */
#define LCD_CLEARDISPLAY 0x01
#define LCD_RETURNHOME 0x02
#define LCD_ENTRYMODESET 0x04
#define LCD_DISPLAYCONTROL 0x08
#define LCD_CURSORSHIFT 0x10
#define LCD_FUNCTIONSET 0x20
#define LCD_SETCGRAMADDR 0x40
#define LCD_SETDDRAMADDR 0x80

/*!
 *  @brief flags for display entry mode
 */
#define LCD_ENTRYRIGHT 0x00
#define LCD_ENTRYLEFT 0x02
#define LCD_ENTRYSHIFTINCREMENT 0x01
#define LCD_ENTRYSHIFTDECREMENT 0x00

/*!
 *  @brief flags for display on/off control
 */
#define LCD_DISPLAYON 0x04
#define LCD_DISPLAYOFF 0x00
#define LCD_CURSORON 0x02
#define LCD_CURSOROFF 0x00
#define LCD_BLINKON 0x01
#define LCD_BLINKOFF 0x00

/*!
 *  @brief flags for display/cursor shift
 */
#define LCD_DISPLAYMOVE 0x08
#define LCD_CURSORMOVE 0x00
#define LCD_MOVERIGHT 0x04
#define LCD_MOVELEFT 0x00

/*!
 *  @brief flags for function set
 */
#define LCD_8BITMODE 0x10
#define LCD_4BITMODE 0x00
#define LCD_2LINE 0x08
#define LCD_1LINE 0x00
#define LCD_5x10DOTS 0x04
#define LCD_5x8DOTS 0x00

class DFRobot_RGBLCD1602 : public Print 
{

public:

  /**
   *  @brief Constructor
   */
  DFRobot_RGBLCD1602(uint8_t lcdCols,uint8_t lcdRows,TwoWire *pWire=&Wire,uint8_t lcdAddr=LCD_ADDRESS,uint8_t RGBAddr=RGB_ADDRESS);

  /**
   *  @brief initialize the LCD and master IIC
   */ 
  void init();

  /**
   *  @brief clear the display and return the cursor to the initial position (position 0)
   */
  void clear();

  /**
   *  @brief return the cursor to the initial position (0,0)
   */
  void home();

    /**
     *  @brief Turn off the display
     */
  void noDisplay();

  /**
   *  @brief Turn on the display
   */
  void display();

  /**
   *  @brief Turn  off the blinking showCursor
   */
  void stopBlink();

  /**
   *  @brief Turn on  the blinking showCursor
   */
  void blink();

  /**
   *  @brief Turn off the underline showCursor 
   */
  void noCursor();

  /**
   *  @brief Turn on the underline showCursor 
   */
  void cursor();

  /**
   *  @brief scroll left to display
   */
  void scrollDisplayLeft();

  /**
   *  @brief scroll right to display
   */
  void scrollDisplayRight();
 
  /**
   *  @brief This is for text that flows Left to Right
   */
  void leftToRight();
 
  /**
   *  @brief This is for text that flows Right to Left
   */
  void rightToLeft();

  /**
   *  @brief This will 'left justify' text from the showCursor
   */
  void noAutoscroll();
 
  /**
   *  @brief This will 'right justify' text from the showCursor
   */
  void autoscroll();
   
  /**
   *  @brief Allows us to fill the first 8 CGRAM locations with custom characters
   *  @param location substitute character range (0-7)
   *  @param charmap  character array the size is 8 bytes
   */
  void customSymbol(uint8_t location, uint8_t charmap[]);

  /**
   *  @brief set cursor position
   *  @param col columns optional range 0-15
   *  @param row rows optional range 0-1，0 is the first row, 1 is the second row
   */
  void setCursor(uint8_t col, uint8_t row);
  
  /**
   *  @brief set RGB
   *  @param r  red   range(0-255)
   *  @param g  green range(0-255)
   *  @param b  blue  range(0-255)
   */
  void setRGB(uint8_t r, uint8_t g, uint8_t b);

  /**
   *  @brief set backlight PWM output
   *  @param color  backlight color  Preferences：REG_RED\REG_GREEN\REG_BLUE
   *  @param pwm  color intensity   range(0-255)
   */
  void setPWM(uint8_t color, uint8_t pwm){setReg(color, pwm);}      // set pwm

  /**
   *  @brief backlight color
   *  @param color  backlight color  Preferences： WHITE\RED\GREEN\BLUE
   */
  void setColor(uint8_t color);

  /**
   *  @brief close the backlight
   */
  void closeBacklight(){setRGB(0, 0, 0);}

  /**
   *  @brief set the backlight to white
   */
  void setColorWhite(){setRGB(255,255 , 255);}

  /**
   *  @brief blink the LED backlight
   */
  void blinkLED(void);

  /**
   *  @brief the LED backlight doesn't blink
   */
  void noBlinkLED(void);

  /**
   *  @brief write character
   *  @param data the written data
   */
  virtual size_t write(uint8_t data);

  /**
   *  @brief send command
   *  @param data the sent command
   */
  void command(uint8_t data);

  /**
   *  @brief set the backlight
   *  @param mode  true indicates the backlight is turned on and set to white, false indicates the backlight is turned off
   */
  void setBacklight(bool mode);

  using Print::write;
  
private:
  /**
   *  @brief the initialization function
   *  @param row rows optional range 0-1，0 is the first row, 1 is the second row
   *  @param charSize  character size LCD_5x8DOTS\LCD_5x10DOTS
   */
  void begin(uint8_t rows, uint8_t charSize = LCD_5x8DOTS);

  /**
   *  @brief set cursor
   *  @param data the data to send
   *  @param len length of the data
   */
  void send(uint8_t *data, uint8_t len);

  /**
   *  @brief set the register
   *  @param addr register address
   *  @param data data
   */
  void setReg(uint8_t addr, uint8_t data);
  uint8_t _showFunction;
  uint8_t _showControl;
  uint8_t _showMode;
  uint8_t _initialized;
  uint8_t _numLines,_currLine;
  uint8_t _lcdAddr;
  uint8_t _RGBAddr;
  uint8_t _cols;
  uint8_t _rows;
  TwoWire *_pWire;
};

#endif
