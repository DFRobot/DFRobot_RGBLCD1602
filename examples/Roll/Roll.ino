/*!
 * @file Roll.ino
 * @brief Roll show 'hello, world!'.
 * @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @licence     The MIT License (MIT)
 * @maintainer [yangfeng](feng.yang@dfrobot.com)
 * @version  V1.0
 * @date  2021-09-24
 * @url https://github.com/DFRobot/DFRobot_RGBLCD1602
 */
#include "DFRobot_RGBLCD1602.h"

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
    // Print a message to the LCD.
    lcd.print("hello, world!");
    delay(1000);
}

void loop() {
    // scroll 13 positions (string length) to the left
    // to move it offscreen left:
    for (int positionCounter = 0; positionCounter < 13; positionCounter++) {
        /**
         *  @brief scroll left to display
         */
        lcd.scrollDisplayLeft();//scroll one position left
        // wait a bit:
        delay(150);
    }

    // scroll 29 positions (string length + show length) to the right
    // to move it offscreen right:
    for (int positionCounter = 0; positionCounter < 29; positionCounter++) {
        /**
         *  @brief scroll right to display
         */
        lcd.scrollDisplayRight();//scroll one position right
        // wait a bit:
        delay(150);
    }

    // scroll 16 positions (show length + string length) to the left
    // to move it back to center:
    for (int positionCounter = 0; positionCounter < 16; positionCounter++) {
        // scroll one position left:
        lcd.scrollDisplayLeft();
        // wait a bit:
        delay(150);
    }

    // delay at the end of the full loop:
    delay(1000);

}

