/*!
 * @file SetColor.ino
 * @brief SetColor.
 * @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @licence     The MIT License (MIT)
 * @maintainer [yangfeng](feng.yang@dfrobot.com)
 * @version  V1.0
 * @date  2021-09-24
 * @url https://github.com/DFRobot/DFRobot_RGBLCD1602
 */
#include "DFRobot_RGBLCD1602.h"

char dtaUart[15];
char dtaLen = 0;

DFRobot_RGBLCD1602 lcd(/*lcdCols*/16,/*lcdRows*/2);  //16 characters and 2 lines of show

void setup() {
	Serial.begin(115200);
    /**
     *  @brief initialize the LCD and master IIC
     */ 
    lcd.init();
    // Print a message to the LCD.
    lcd.print("set cllor");
}

void loop() {
    if(dtaLen == 11) {
        int r = (dtaUart[0]-'0')*100 + (dtaUart[1] - '0')*10 + (dtaUart[2] - '0');          // get r
        int g = (dtaUart[4]-'0')*100 + (dtaUart[5] - '0')*10 + (dtaUart[6] - '0');
        int b = (dtaUart[8]-'0')*100 + (dtaUart[9] - '0')*10 + (dtaUart[10] - '0');
        
        dtaLen = 0;
        /**
         *  @brief set RGB
         *  @param r  red   range(0-255)
         *  @param g  green range(0-255)
         *  @param b  blue  range(0-255)
         */
        lcd.setRGB(r, g, b);

        Serial.println("get data");
        
        Serial.println(r);
        Serial.println(g);
        Serial.println(b);
        Serial.println();

    }
}

void serialEvent() {
    while(Serial.available()) {
        dtaUart[dtaLen++] = Serial.read();
    }
}

