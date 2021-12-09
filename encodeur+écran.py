from rpi_lcd import LCD
from RPi import GPIO
from time import sleep

lcd= LCD()
push= 5
clk = 13
dt = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(push, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
counter = 0
clkLastState= GPIO.input(clk)

a=['do', 'ré', 'mi', 'fa','sol','la','si']
notes=[]
for i in range(100):
    for j in range(len(a)):
        notes.append(a[j])

try:
        while True:
                etat = GPIO.input(push)
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        lcd.text(str(counter),1)
                        lcd.text(notes[counter//5],2)
                        print(counter)
                if (etat == 0):
                    if counter !=0:
                        counter = 0
                        lcd.text(str(counter),1)
                        lcd.text("Appui detect",2)
                        sleep(1)
                        lcd.clear()    
                clkLastState = clkState
finally:
        GPIO.cleanup()