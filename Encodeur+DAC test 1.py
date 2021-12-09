import RPi.GPIO as GPIO
from time import sleep
import Adafruit_MCP4725
dac = Adafruit_MCP4725.MCP4725(address=0x60)

GPIO.setmode(GPIO.BCM) #Pour détecter quel système de numérotation des pins on utilise
GPIO.setwarnings(False) #Pour désactiver les avertissements sur les entrées

#Définit les pins utilisé par les encodeurs (n° encodeur,clk,dt,sw). Si on utilise pas le sw, notez False
encoder_1 = (1,13,19,26)
encoder_2 = (2,5,6,False)
encoder_3 = (3,10,11,False)
encoder_4 = (4,20,21,False)
encoder_5 = (5,12,16,False)
encoder_6 = (6,8,7,False)
encoder_7 = (7,24,25,False)
encoder = [encoder_1,encoder_2,encoder_3,encoder_4,encoder_5,encoder_6,encoder_7]

#configure chaque canal comme entrée ou sortie
for enc in encoder :
    GPIO.setup(enc[1], GPIO.IN)
    GPIO.setup(enc[2], GPIO.IN)
    if enc[3] != False :
        GPIO.setup(enc[3], GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Définit l'action des boutons
Bouton_1 = 'Mahir == Force'
Bouton_2 = 'Julien == Force'
Bouton_3 = 'Nicolas == Force'
Bouton_4 = 'Philippe == Force'
Bouton_5 = 'Eliott == Force'
Bouton_6 = 'Nathan == Force'
Bouton_7 = 'Info 2 == Force'
Action_Bouton = [Bouton_1,Bouton_2,Bouton_3,Bouton_4,Bouton_5,Bouton_6,Bouton_7]

#Définit les valeurs initiales des encodeurs
val = [0,0,0,0,0,0,0]

#Définit les paliers en fonction des encodeurs
step = [int(4096/5),1,1,1,1,1,1]

#pDéfinit l'intervalle des encodeurs
interval = [(0,4096),(-20,20),(-20,20),(-20,20),(-20,20),(-20,20),(-20,20)]

a_pre,b_pre,bouton_pre = 1,1,False

def set_value_dac() :
    global val
    dac.set_voltage(val[0])

def encodeur(num,clk,dt,sw) :
    global step, interval, val, Action_Bouton, a_pre, b_pre, bouton_pre
    a, b = GPIO.input(clk), GPIO.input(dt)
    if sw != False :
        bouton = not GPIO.input(sw)
        if bouton != bouton_pre :
            if bouton == True :
                print(Action_Bouton[num-1])
            bouton_pre = bouton
            sleep(0.05)
    if a != a_pre or b != b_pre:
        if a == 0 and b == 1 :
            while not (a == 1 and b == 1):
                a, b = GPIO.input(clk), GPIO.input(dt)
            if val[num-1] != interval[num-1][1] :
                val[num-1] += step[num-1]

        if a == 1 and b == 0 :
            while not (a == 1 and b == 1):
                a, b = GPIO.input(clk), GPIO.input(dt)
            if val[num-1] != interval[num-1][0] :
                val[num-1] -= step[num-1]

        a_pre,b_pre = a,b
    set_value_dac()



try :
    while True :
        for num in range(len(encoder)) :
            encodeur(num+1,encoder[num][1],encoder[num][2],encoder[num][3])

except KeyboardInterrupt:
    print('\nScript end!')

finally:
    GPIO.cleanup()