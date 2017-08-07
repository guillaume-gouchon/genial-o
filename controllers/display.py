from RPLCD import CharLCD, cleared, cursor

# lcd = CharLCD()

def setLeftLed(enabled):
    print('setLeftLed', enabled)
    raspiRobotBoard.set_led1(1 if enabled else 0);

def setRightLed(enabled):
    print('setRightLed', enabled)
    raspiRobotBoard.set_led2(1 if enabled else 0);

def printText(text, line):
    print('printText', text, 'line=', line)
    with cursor(lcd, --line, 0):
        lcd.write_string(text)
