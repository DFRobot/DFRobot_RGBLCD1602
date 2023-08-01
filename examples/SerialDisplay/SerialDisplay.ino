/*!
 * @file SerialDisplay.ino
 * @brief Read serial port and display.
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
  LCD1602 RGB Module  |  V2.0  | 0x2D   |
-----------------------------------------
*/

DFRobot_RGBLCD1602 lcd(/*RGBAddr*/0x60 ,/*lcdCols*/16,/*lcdRows*/2);  //16 characters and 2 lines of show

void setup() {
    /**
     *  @brief initialize the LCD and master IIC
     */ 
    lcd.init();
    // initialize the serial communications:
    Serial.begin(9600);
}

void loop() {
    // when characters arrive over the serial port...
    if (Serial.available()) {
        // wait a bit for the entire message to arrive
        delay(100);
       /**
        *  @brief clear the display and return the cursor to the initial position (position 0)
        */
        lcd.clear();
        // read all the available characters
        while (Serial.available() > 0) {
            // display each character to the LCD
            lcd.write(Serial.read());
        }
    }
}

