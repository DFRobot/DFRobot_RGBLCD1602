# DFRobot_RGBLCD1602
- [English Version](./README.md)

见惯了千篇一律的LCD液晶屏，你是否也想来一次不一样的体验？DFRobot彩光LCD将给您带来全新的视觉感受，摆脱沉闷的单色背光，换上RGB全彩背光，能够提供1600万种颜色组合。 DFRobot Gravity I2C LCD1602彩色背光液晶屏采用通用Gravity i2C接口，仅需两根通信线，即可完成通信与背光控制。液晶屏可以显示2x16个字符，支持屏幕滚动，光标移动等功能。没有繁琐的接线，没有复杂的代码，通过专门的Raspberrypi库，就可以完成所有的设计。



![](../../resources/images/DFR0464.jpg)
![](../../resources/images/DFR0557.png)

## 产品链接(https://www.dfrobot.com.cn/goods-1419.html)

    SKU：DFR0464

## 目录

* [概述](#概述)
* [库安装](#库安装)
* [方法](#方法)
* [兼容性](#兼容性)
* [历史](#历史)
* [创作者](#创作者)

## 概述

DFRobot Gravity I2C LCD1602彩色背光液晶屏可以显示2x16个字符，支持屏幕滚动，光标移动，背光颜色调节等功能

## 库安装

使用此库前，请首先下载库文件，将其粘贴到树莓派的自定义目录中，然后打开examples文件夹并在该文件夹中运行演示。
本库使用到了wiringpi，使用本库前先检查树莓派是否导入了wiringpi，若没有导入先请导入
python2: pip install wiringpi
python3: pip3 install wiringpi

## 方法

```Python

  def write(self,data)
    '''
      @brief write character
      @param data 写入的数据
    '''

  def set_RGB(self,r,g,b)
    '''
      @brief 设置RGB
      @param r  red   范围(0-255)
      @param g  green 范围(0-255)
      @param b  blue  范围(0-255)
    '''

  def set_cursor(self,col,row)
    '''
      @brief 设置光标位置
      @param col 列数 可选范围 0-15
      @param row 行数 可选范围 0-1，0代表了第一行，1代表了第二行
    '''

  def clear(self)
    '''
      @brief 清除显示并将光标回到初始位置（0位置）
    '''

  def scroll_display_left(self)
    '''
      @brief 向左滚动显示
    '''

  def scroll_display_right(self)
    '''
      @brief 向右滚动显示
    '''

  def print_out(self,arg)
    '''
      @brief 向液晶屏输出显示
      @param arg 输出的数据
    '''

  def home(self)
    '''
      @brief 将光标回到初始位置（0,0）
    '''

  def no_display(self)
    '''
      @brief 关闭显示
    '''

  def display(self)
    '''
      @brief 打开显示
    '''

  def stop_blink(self)
    '''
      @brief 关闭闪烁光标
    '''

  def blink(self)
    '''
      @brief 打开闪烁光标
    '''

  def no_cursor(self)
    '''
      @brief 关闭下划线光标
    '''

  def cursor(self)
    '''
      @brief 打开下划线光标
    '''

  def left_to_right(self)
    '''
      @brief 此函数用于从左到右流动的文本
    '''

  def right_to_left(self)
    '''
      @brief 此函数用于从右到左流动的文本
    '''

  def no_autoscroll(self)
    '''
      @brief 这将使文本从显示光标处“左对齐”
    '''

  def autoscroll(self)
    '''
      @brief 这将使文本从显示光标处“右对齐”
    '''

  def custom_symbol(self,location, charmap)
    '''
      @brief 允许我们将前8个CGRAM位置填充自定义字符
      @param location 代替字符 范围（0-7）
      @param charmap  字符列表 大小8个字节
    '''

  def set_backlight(self,mode)
    '''
      @brief 设置背光
      @param mode  true代表开启背光并设置为白色，false代表关闭背光
    '''

  def set_pwm(self,color,pwm)
    '''
       @brief 设置背光PWM输出
       @param color  背光颜色  参数选择：REG_RED\REG_GREEN\REG_BLUE
       @param pwm  颜色强度值   范围(0-255)
    '''

  def set_color_white(self)
    '''
       @brief 设置背光为白色
    '''

  def close_backlight(self)
    '''
      @brief 关闭背光
    '''
```

## 兼容性

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |     √     |            |          |         |
| RaspberryPi4 |           |            |    √     |         |

* Python 版本

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |


## 历史

- 日期 2021-9-26
- 版本 V1.0.0


## 创作者

Written by yangfeng(feng.yang@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))

