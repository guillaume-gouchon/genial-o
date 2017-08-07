from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x3f)

def setLeftLed(enabled):
    print('setLeftLed', enabled)
    raspiRobotBoard.set_led1(1 if enabled else 0);

def setRightLed(enabled):
    print('setRightLed', enabled)
    raspiRobotBoard.set_led2(1 if enabled else 0);

def printText(text, line):
    print('printText', text, 'line=', line)
    lcd.write_string(text)
