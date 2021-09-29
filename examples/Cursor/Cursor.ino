/*!
 * @file Cursor.ino
 * @brief cursor.
 * @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @licence     The MIT License (MIT)
 * @maintainer [yangfeng](feng.yang@dfrobot.com)
 * @version  V1.0
 * @date  2021-09-24
 * @url https://github.com/DFRobot/DFRobot_RGBLCD1602
 */

#include "DFRobot_RGBLCD1602.h"

DFRobot_RGBLCD1602 lcd(/*lcdCols*/16,/*lcdRows*/2);  //16 characters and 2 lines of show

void setup() {
    /**
     *  @brief initialize the LCD and master IIC
     */ 
    lcd.init();

    // Print a message to the LCD.
    lcd.print("hello, world!");
}

void loop() {
    /**
     *  @brief Turns the underline showCursor off
     */
    lcd.noCursor();// Turn off the cursor
    delay(500);

    /**
     *  @brief Turns the underline showCursor on
     */
    lcd.cursor();// Turn on the cursor
    delay(500);
}

