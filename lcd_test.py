from rpi_lcd import LCD
import time

lcd = LCD()

def clignote():
    val = True
    n = 0
    while val:
        lcd.text("Projet synthe ",1)
        lcd.text("TranH201",2)
        time.sleep(2.0)
        lcd.clear()
        time.sleep(0.5)
        n += 1
        if n == 5:
            lcd.text("Au revoir",1)
            time.sleep(1)
            val = False

def date():
    while True:
        lcd.text("Date: %s" %time.strftime("%d/%m/%Y"),1)
        lcd.text("Heure: %s" %time.strftime("%H:%M:%S"),2)

def inpu_t():
    while True:
        lcd.text("'exit' to stop",2)
        u = input("texte (16 char. max): ")
        if u != "exit":
            n = float(input("temps affiché (s): "))
            lcd.text(u,1)
            time.sleep(n)
            lcd.clear()
        if u == "exit":
            lcd.clear()
            lcd.text(u,1)
            time.sleep(2)
            break
        

#clignote()
#date()
#inpu_t()
lcd.clear()