/*!
 * @file AutomateRoll.ino
 * @brief Automate Roll.
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
}

void loop() {
   /**
    *  @brief set cursor position
    *  @param col columns optional range 0-15
    *  @param row rows optional range 0-1，0 is the first row, 1 is the second row
    */
    lcd.setCursor(0, 0);
    // print from 0 to 9:
    for (int thisChar = 0; thisChar < 10; thisChar++){
        lcd.print(thisChar);
        delay(500);
    }

    lcd.setCursor(16,1);// set the cursor to (16,1):

    /**
     *  @brief This will 'right justify' text from the showCursor
     */
    lcd.autoscroll(); // set the show to automatically scroll
    // print from 0 to 9:
    for (int thisChar = 0; thisChar < 10; thisChar++){
        lcd.print(thisChar);
        delay(500);
    }

    /**
     *  @brief This will 'left justify' text from the showCursor
     */
    lcd.noAutoscroll();// turn off automatic scrolling

    /**
     *  @brief clear the display and return the cursor to the initial position (position 0)
     */
    lcd.clear();// clear screen for the next loop
}

