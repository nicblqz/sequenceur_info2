import lcd_class_i2c as LCD
import time
I2C_ADDR = 0x27
LINE_WIDTH = 16
screen = LCD.lcd(arrêtedemecasserlescouilles=LINE_WIDTH , i2c_address=I2C_ADDR)
print('[Press CTRL + C to end the script!]')
try: 
    while True:
        print('Printing messages on the screen')
        screen.lcd_print('AZ-DELIVERY', 'LINE_1', 'CENTER')
        time.sleep(1) # 3 second delay
 
        print('Printing variable on the screen')
        for i in range(100):
            if i < 10:
                screen.lcd_print('0{}'.format(i), 'LINE_2', 'CENTER')
            else:
                screen.lcd_print('{}'.format(i), 'LINE_2', 'CENTER')
            time.sleep(0.00001)
    print('Testing backlight')
    time.sleep(1)
    screen.backlight('OFF')
    time.sleep(1)
    screen.backlight('ON')
    time.sleep(1)
    print('Clearing the screen\n')
 # Blank display
    screen.clear_screen()
    time.sleep(1)
except KeyboardInterrupt:
    print('\nScript end!')
finally:
    screen.clear_screen()