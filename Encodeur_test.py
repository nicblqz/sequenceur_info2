import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) #Pour détecter quel système de numérotation des pins on utilise
GPIO.setwarnings(False) #Pour désactiver les avertissements sur les entrées

#Définit les pins utilisé par les encodeurs (n° encodeur,clk,dt,sw). Si on utilise pas le sw, notez False
encoder_1 = (1,2,3,4)
encoder_2 = (2,17,27,22)
#encoder_3 = (3,10,9,11)
#encoder_4 = (4,0,1,False)
#encoder_5 = (5,0,1,False)
#encoder_6 = (6,0,1,False)
#encoder_7 = (7,0,1,False)
encoder = [encoder_1,encoder_2]
#,encoder_3,encoder_4,encoder_5,encoder_6,encoder_7]

#configure chaque canal comme entrée ou sortie
for enc in encoder :
    GPIO.setup(enc[1], GPIO.IN)
    GPIO.setup(enc[2], GPIO.IN)
    if enc[3] != False :
        GPIO.setup(enc[3], GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Définit les valeurs initiales des encodeurs
val = [0,0,0,0,0,0,0]

#Définit les paliers en fonction des encodeurs
step = [1,1,1,1,1,1,1]

#pDéfinit l'intervalle des encodeurs
interval = [(-20,20),(-20,20),(-20,20),(-20,20),(-20,20),(-20,20),(-20,20)]

a_pre,b_pre,bouton_pre = 1,1,False

def encodeur(num,clk,dt,sw) :
    global step, interval, val, a_pre, b_pre, bouton_pre
    pause = False
    a, b = GPIO.input(clk), GPIO.input(dt)
    bouton = not GPIO.input(sw)
    if sw != False :
        if bouton != bouton_pre and pause == False :
            print(bouton)
            bouton_pre = bouton
            sleep(0.01)
    if a != a_pre or b != b_pre:
        if a == 0 and b == 1 and pause == False :
            if val[num-1] != interval[num-1][1] :
                val[num-1] += step[num-1]
            pause = True
            print('{}|{}|{}|{}|{}|{}|{}'.format('V1 =' + val[0], 'V2 =' + val[1], 'V3 =' + val[2], 'V4 =' + val[3],
                                                'V5 =' + val[4], 'V6 =' + val[5], 'V7 =' + val[6]))
        if a == 1 and b == 0 and pause == False :
            if val[num-1] != interval[num-1][0] :
                val[num-1] -= step[num-1]
            pause = True
            print('{}|{}|{}|{}|{}|{}|{}'.format('V1 =' + val[0], 'V2 =' + val[1], 'V3 =' + val[2], 'V4 =' + val[3],
                                                'V5 =' + val[4], 'V6 =' + val[5], 'V7 =' + val[6]))
        if a== 0 and b == 0 and pause == True :
            pause = False
        a_pre,b_pre = a,b

try :
    while True :
        for num in range(len(encoder)) :
            encodeur(num+1,encoder[num][1],encoder[num][2],encoder[num][3])

except KeyboardInterrupt:
    print('\nScript end!')

finally:
    GPIO.cleanup()