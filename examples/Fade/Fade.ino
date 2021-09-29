/*!
 * @file Fade.ino
 * @brief Fade.
 * @copyright	Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @licence     The MIT License (MIT)
 * @maintainer [yangfeng](feng.yang@dfrobot.com)
 * @version  V1.0
 * @date  2021-09-24
 * @url https://github.com/DFRobot/DFRobot_RGBLCD1602
 */
#include "DFRobot_RGBLCD1602.h"

DFRobot_RGBLCD1602 lcd(/*lcdCols*/16,/*lcdRows*/2);  //16 characters and 2 lines of show

void breath(unsigned char color){
    for(int i=0; i<255; i++){
        /**
         *  @brief set backlight PWM output
         *  @param color  backlight color  Preferences：REG_RED\REG_GREEN\REG_BLUE
         *  @param pwm  color intensity   range(0-255)
         */
        lcd.setPWM(color, i);
        delay(5);
    }

    delay(500);
    for(int i=254; i>=0; i--){
        lcd.setPWM(color, i);
        delay(5);
    }

    delay(500);
}

void setup() {
    /**
     *  @brief initialize the LCD and master IIC
     */ 
    lcd.init();
    // Print a message to the LCD.
    lcd.print("fade demo");

}

void loop() {
    breath(REG_RED);
    breath(REG_GREEN);
    breath(REG_BLUE);
}

