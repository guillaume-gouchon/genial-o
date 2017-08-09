from RPLCD.i2c import CharLCD
from board import raspi_robot_board

LCD_PORT_EXPANDER = "PCF8574"
LCD_DISPLAY_ADDRESS = 0x3f
lcd = CharLCD(LCD_PORT_EXPANDER, LCD_DISPLAY_ADDRESS)

# create degree character
degree = (
    0b00111,
    0b00101,
    0b00111,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
)
lcd.create_char(1, degree)

def set_left_led(enabled):
    print("set_left_led", enabled)
    raspi_robot_board.set_led1(1 if enabled else 0);

def set_right_led(enabled):
    print("set_right_led", enabled)
    raspi_robot_board.set_led2(1 if enabled else 0);

def clear_text():
    lcd.clear()

def print_text(text, line):
    print("print_text", text, "line=", line)
    lcd.cursor_pos = (line - 1, 0)
    lcd.write_string("                    ");
    lcd.cursor_pos = (line - 1, 0)
    lcd.write_string(str(text))
