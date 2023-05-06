/*!
 * @file TextDirection.ino
 * @brief TextDirection.
 * @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @licence     The MIT License (MIT)
 * @maintainer [yangfeng](feng.yang@dfrobot.com)
 * @version  V1.0
 * @date  2021-09-24
 * @url https://github.com/DFRobot/DFRobot_RGBLCD1602
 */
#include "DFRobot_RGBLCD1602.h"

int thisChar = 'a';

/*
Change the RGBaddr value based on the hardware version
-----------------------------------------
       Moudule        | Version| RGBAddr|
-----------------------------------------
  LCD1602 Module      |  V1.0  | 0x60   |
-----------------------------------------
  LCD1602 Module      |  V1.1  | 0x6B   |
-----------------------------------------
  LCD1602 RGB Module  |  V1.0  | 0x60   |
-----------------------------------------
  LCD1602 RGB Module  |  V1.1  | 0x2D   |
-----------------------------------------
*/

DFRobot_RGBLCD1602 lcd(/*RGBAddr*/0x60 ,/*lcdCols*/16,/*lcdRows*/2);  //16 characters and 2 lines of show

void setup() {
    /**
     *  @brief initialize the LCD and master IIC
     */ 
    lcd.init();
    /**
     *  @brief Turn on the underline showCursor 
     */
    lcd.cursor();
}

void loop() {
    // reverse directions at 'm':
    if (thisChar == 'm') {
        /**
         *  @brief This is for text that flows Right to Left
         */
        lcd.rightToLeft();// go right for the next letter
    }
    // reverse again at 's':
    if (thisChar == 's') {
        /**
         *  @brief This is for text that flows Left to Right
         */
        lcd.leftToRight();// go left for the next letter
    }
    // reset at 'z':
    if (thisChar > 'z') {
        /**
         *  @brief return the cursor to the initial position（0,0）
         */
        lcd.home();
        // start again at 0
        thisChar = 'a';
    }
    // print the character
    lcd.write(thisChar);
    // wait a second:
    delay(1000);
    // increment the letter:
    thisChar++;
}

