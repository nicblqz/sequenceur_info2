from RPi import GPIO
from time import sleep
push= 5
clk = 13
dt = 6
push2 = 26
clk2 = 17
dt2 = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(push, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(push2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
counter = 0
clkLastState = GPIO.input(clk)
clkLastState2 = GPIO.input(clk2)
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
                        print(counter)
                if (etat == 0):
                    if counter !=0:
                        counter = 0
                        print("Appui detect")
                        print(counter)
                clkLastState = clkState
                etat2 = GPIO.input(push2)
                clkState2 = GPIO.input(clk2)
                dtState2 = GPIO.input(dt2)
                if clkState2 != clkLastState2:
                        if dtState2 != clkState2:
                                counter -= 1
                        else:
                                counter += 1
                        print(counter)
                if (etat2 == 0):
                    if counter !=0:
                        counter = 0
                        print("Appui detect")
                        print(counter)
                clkLastState2 = clkState2
finally:
        GPIO.cleanup()

