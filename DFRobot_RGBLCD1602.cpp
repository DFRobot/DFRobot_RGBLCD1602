/*!
 * @file DFRobot_RGBLCD1602.cpp
 * @brief DFRobot_RGBLCD1602 class infrastructure, the implementation of basic methods
 * @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @licence     The MIT License (MIT)
 * @maintainer [yangfeng](feng.yang@dfrobot.com)
 * @version  V1.0
 * @date  2021-09-24
 * @url https://github.com/DFRobot/DFRobot_RGBLCD1602
 */

#include <stdio.h>
#include <string.h>


#include "DFRobot_RGBLCD1602.h"

const uint8_t color_define[4][3] = 
{
    {255, 255, 255},            // white
    {255, 0, 0},                // red
    {0, 255, 0},                // green
    {0, 0, 255},                // blue
};

/*******************************public*******************************/
DFRobot_RGBLCD1602::DFRobot_RGBLCD1602(uint8_t RGBAddr,uint8_t lcdCols,uint8_t lcdRows,TwoWire *pWire,uint8_t lcdAddr)
{
  _lcdAddr = lcdAddr;
  _RGBAddr = RGBAddr;
  _cols = lcdCols;
  _rows = lcdRows;
  _pWire = pWire;
}

void DFRobot_RGBLCD1602::init()
{
  _pWire->begin();
  if(_RGBAddr == (0x60)){
    REG_RED   =      0x04;
    REG_GREEN =      0x03;
    REG_BLUE  =      0x02;
    REG_ONLY  =      0x02 ;
  } else if(_RGBAddr == (0x60>>1)){
    REG_RED      =   0x06 ;       // pwm2
    REG_GREEN    =   0x07 ;       // pwm1
    REG_BLUE     =   0x08 ;       // pwm0
    REG_ONLY     =   0x08 ;
  } else if(_RGBAddr == (0x6B)){
    REG_RED      =   0x06 ;       // pwm2
    REG_GREEN    =   0x05 ;       // pwm1
    REG_BLUE     =   0x04 ;       // pwm0
    REG_ONLY     =   0x04 ; 
  } else if(_RGBAddr == (0x2D)){
    REG_RED      =   0x01 ;       // pwm2
    REG_GREEN    =   0x02 ;       // pwm1
    REG_BLUE     =   0x03 ;       // pwm0
    REG_ONLY     =   0x01 ; 
  }
  _showFunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS;
  begin(_rows);
}

void DFRobot_RGBLCD1602::clear()
{
    command(LCD_CLEARDISPLAY);        // clear display, set cursor position to zero
    delayMicroseconds(2000);          // this command takes a long time!
}

void DFRobot_RGBLCD1602::home()
{
    command(LCD_RETURNHOME);        // set cursor position to zero
    delayMicroseconds(2000);        // this command takes a long time!
}

void DFRobot_RGBLCD1602::noDisplay()
{
    _showControl &= ~LCD_DISPLAYON;
    command(LCD_DISPLAYCONTROL | _showControl);
}

void DFRobot_RGBLCD1602::display() {
    _showControl |= LCD_DISPLAYON;
    command(LCD_DISPLAYCONTROL | _showControl);
}

void DFRobot_RGBLCD1602::stopBlink()
{
    _showControl &= ~LCD_BLINKON;
    command(LCD_DISPLAYCONTROL | _showControl);
}
void DFRobot_RGBLCD1602::blink()
{
    _showControl |= LCD_BLINKON;
    command(LCD_DISPLAYCONTROL | _showControl);
}

void DFRobot_RGBLCD1602::noCursor()
{
    _showControl &= ~LCD_CURSORON;
    command(LCD_DISPLAYCONTROL | _showControl);
}

void DFRobot_RGBLCD1602::cursor() {
    _showControl |= LCD_CURSORON;
    command(LCD_DISPLAYCONTROL | _showControl);
}

void DFRobot_RGBLCD1602::scrollDisplayLeft(void)
{
    command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT);
}

void DFRobot_RGBLCD1602::scrollDisplayRight(void)
{
    command(LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT);
}

void DFRobot_RGBLCD1602::leftToRight(void)
{
    _showMode |= LCD_ENTRYLEFT;
    command(LCD_ENTRYMODESET | _showMode);
}

void DFRobot_RGBLCD1602::rightToLeft(void)
{
    _showMode &= ~LCD_ENTRYLEFT;
    command(LCD_ENTRYMODESET | _showMode);
}

void DFRobot_RGBLCD1602::noAutoscroll(void)
{
    _showMode &= ~LCD_ENTRYSHIFTINCREMENT;
    command(LCD_ENTRYMODESET | _showMode);
}

void DFRobot_RGBLCD1602::autoscroll(void)
{
    _showMode |= LCD_ENTRYSHIFTINCREMENT;
    command(LCD_ENTRYMODESET | _showMode);
}

void DFRobot_RGBLCD1602::customSymbol(uint8_t location, uint8_t charmap[])
{

    location &= 0x7; // we only have 8 locations 0-7
    command(LCD_SETCGRAMADDR | (location << 3));
    
    
    uint8_t data[9];
    data[0] = 0x40;
    for(int i=0; i<8; i++)
    {
        data[i+1] = charmap[i];
    }
    send(data, 9);
}

void DFRobot_RGBLCD1602::setCursor(uint8_t col, uint8_t row)
{

    col = (row == 0 ? col|0x80 : col|0xc0);
    uint8_t data[3] = {0x80, col};

    send(data, 2);

}

void DFRobot_RGBLCD1602::setRGB(uint8_t r, uint8_t g, uint8_t b)
{
  uint16_t temp_r,temp_g,temp_b;
  if(_RGBAddr == 0x60>>1){
    temp_r = (uint16_t)r*192/255;
    temp_g = (uint16_t)g*192/255;
    temp_b = (uint16_t)b*192/255;
    setReg(REG_RED, temp_r);
    setReg(REG_GREEN, temp_g);
    setReg(REG_BLUE, temp_b);
  } else{
    setReg(REG_RED, r);
    setReg(REG_GREEN, g);
    setReg(REG_BLUE, b);
    if(_RGBAddr == 0x6B){
      setReg(0x07, 0xFF);
    }
  }

}

void DFRobot_RGBLCD1602::setColor(uint8_t color)
{
    if(color > 3)return ;
    setRGB(color_define[color][0], color_define[color][1], color_define[color][2]);
}


inline size_t DFRobot_RGBLCD1602::write(uint8_t value)
{

    uint8_t data[3] = {0x40, value};
    send(data, 2);
    return 1; // assume sucess
}

inline void DFRobot_RGBLCD1602::command(uint8_t value)
{
    uint8_t data[3] = {0x80, value};
    send(data, 2);
}



void DFRobot_RGBLCD1602::setBacklight(bool mode){
	if(mode){
		setColorWhite();		// turn backlight on
	}else{
		closeBacklight();		// turn backlight off
	}
}

/*******************************private*******************************/
void DFRobot_RGBLCD1602::begin( uint8_t rows, uint8_t charSize) 
{
    if (rows > 1) {
        _showFunction |= LCD_2LINE;
    }
    _numLines = rows;
    _currLine = 0;
    ///< for some 1 line displays you can select a 10 pixel high font
    if ((charSize != 0) && (rows == 1)) {
        _showFunction |= LCD_5x10DOTS;
    }

    ///< SEE PAGE 45/46 FOR INITIALIZATION SPECIFICATION!
    ///< according to datasheet, we need at least 40ms after power rises above 2.7V
    ///< before sending commands. Arduino can turn on way befer 4.5V so we'll wait 50
    delay(50);

    ///< this is according to the hitachi HD44780 datasheet
    ///< page 45 figure 23

    ///< Send function set command sequence
    command(LCD_FUNCTIONSET | _showFunction);
    delay(5);  // wait more than 4.1ms
	
	///< second try
    command(LCD_FUNCTIONSET | _showFunction);
    delay(5);

    ///< third go
    command(LCD_FUNCTIONSET | _showFunction);

    ///< turn the display on with no cursor or blinking default
    _showControl = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF;
    display();

    ///< clear it off
    clear();

    ///< Initialize to default text direction (for romance languages)
    _showMode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT;
    ///< set the entry mode
    command(LCD_ENTRYMODESET | _showMode);
    
    if(_RGBAddr == (0xc0>>1)){
      ///< backlight init
      setReg(REG_MODE1, 0);
      ///< set LEDs controllable by both PWM and GRPPWM registers
      setReg(REG_OUTPUT, 0xFF);
      ///< set MODE2 values
      ///< 0010 0000 -> 0x20  (DMBLNK to 1, ie blinky mode)
      setReg(REG_MODE2, 0x20);
    }else if(_RGBAddr == (0x60>>1)){
       setReg(0x01, 0x00);
       setReg(0x02, 0xfF);
       setReg(0x04, 0x15);
    }else if(_RGBAddr==0x6B){
        setReg(0x2F, 0x00);
        setReg(0x00, 0x20);
        setReg(0x01, 0x00);
        setReg(0x02, 0x01);
        setReg(0x03, 4);
    }
    setColorWhite();
}

void DFRobot_RGBLCD1602::send(uint8_t *data, uint8_t len)
{
    _pWire->beginTransmission(_lcdAddr);        // transmit to device #4
    for(int i=0; i<len; i++) {
        _pWire->write(data[i]);
		delay(5);
    }
    _pWire->endTransmission();                     // stop transmitting
}

void DFRobot_RGBLCD1602::setReg(uint8_t addr, uint8_t data)
{
    _pWire->beginTransmission(_RGBAddr); // transmit to device #4
    _pWire->write(addr);
    _pWire->write(data);
    _pWire->endTransmission();    // stop transmitting
}



