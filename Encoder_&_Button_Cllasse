import RPi.GPIO as GPIO
from Config_0 import Encodeur, Bouton, GEN, SEQ

# Pour déterminer quel système de numérotation des pins on utilise
GPIO.setmode(GPIO.BCM)


# Classe définissant les encodeurs
class Encoder:

    # IN : le nom de l'encodeur et le numéro des pins clk, dt et sw (None par défaut si pas de sw)
    # Définit l'objet encodeur, PreValue et LastValue sont des valeurs utilent pour la méthode "motion_sensor"
    def __init__(self, name, clk, dt, sw=None):
        self.name = name
        self.clk = clk
        self.dt = dt
        self.sw = sw
        if sw is not None:
            self.PreValue = GPIO.input(sw)
        self.LastValue = [GPIO.input(clk), GPIO.input(dt)]

    # Détecte les actions sur les encodeurs (tourner à gauche/droite et utilisation du bouton poussoir)
    def motion_sensor(self):
        clkvalue: object = GPIO.input(self.clk)
        dtvalue = GPIO.input(self.dt)
        actualvalue = [clkvalue, dtvalue]

        if self.sw is not None:
            buttonvalue = GPIO.input(self.sw)
            if buttonvalue != self.PreValue:
                while not buttonvalue == 0:
                    buttonvalue = GPIO.input(self.sw)
                return "button pressed"

        elif actualvalue != self.LastValue:
            if clkvalue == 0 and dtvalue == 1:
                while not (clkvalue == 1 and dtvalue == 1):
                    clkvalue = GPIO.input(self.clk)
                    dtvalue = GPIO.input(self.dt)
                return "rotated clockwise"

            elif clkvalue == 1 and dtvalue == 0:
                while not (clkvalue == 1 and dtvalue == 1):
                    clkvalue = GPIO.input(self.clk)
                    dtvalue = GPIO.input(self.dt)
                return "rotated counter-clockwise"

    # IN : le signe de la modification +/- qui change si on tourne l'encodeur à gauche ou à droite
    #       et les dictionnaires de valeur GEN et SEQ (voir CONFIG.py)
    # Modifie les valeurs dans les dictionnaires de valeur GEN et SEQ
    def dictionary_modification(self, signe, gen, seq):
        actuel = gen["actuel"]

        if self.name == "encodeur_PARAM":
            if signe is None:
                gen["actuel"][1] = (gen["actuel"][1] + 1) % 3

            elif actuel[1] == 1:
                if 0 <= gen["long"] + float("{}1".format(signe)) <= 64:
                    if actuel[0] > gen["long"] + float("{}1".format(signe)):
                        gen["long"] += float("{}1".format(signe))

            elif actuel[1] == 2:
                if 0 <= gen["bpm"] + float("{}25".format(signe)) <= 500:
                    gen["bpm"] += float("{}25".format(signe))

            elif actuel[1] == 3:
                if 0 <= gen["gam"] + float("{}1".format(signe)) <= 3:
                    gen["gam"] += float("{}1".format(signe))

        elif self.name == "encodeur_NOTE":
            if 1 <= seq["pas".format(actuel[0])]["note"] + float("{}204.8".format(signe)) <= 4096:
                seq["pas".format(actuel[0])]["note"] += float("{}204.8".format(signe))

        elif self.name == "encodeur_GATE":
            if 1 <= seq["pas".format(actuel[0])]["gate"] + float("{}204.8".format(signe)) <= 4096:
                seq["pas".format(actuel[0])]["gate"] += float("{}204.8".format(signe))

        elif self.name == "encodeur_CV1":
            if 1 <= seq["pas".format(actuel[0])]["cv1"] + float("{}204.8".format(signe)) <= 4096:
                seq["pas".format(actuel[0])]["cv1"] += float("{}204.8".format(signe))

        elif self.name == "encodeur_CV2":
            if 1 <= seq["pas".format(actuel[0])]["cv2"] + float("{}204.8".format(signe)) <= 4096:
                seq["pas".format(actuel[0])]["cv2"] += float("{}204.8".format(signe))

        elif self.name == "encodeur_CV3":
            if 1 <= seq["pas".format(actuel[0])]["cv3"] + float("{}204.8".format(signe)) <= 4096:
                seq["pas".format(actuel[0])]["cv3"] += float("{}204.8".format(signe))

        elif self.name == "encodeur_CV4":
            if 1 <= seq["pas".format(actuel[0])]["cv4"] + float("{}204.8".format(signe)) <= 4096:
                seq["pas".format(actuel[0])]["cv4"] += float("{}204.8".format(signe))

        return gen, seq


# Classe définissant les boutons
class Button:

    # IN : le nom du bouton et le numéro de la pin
    # Définit l'objet button, PreValue est une valeur utile pour la méthode "motion_sensor"
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.PreValue = GPIO.input(pin)

    # Détecte les actions sur les boutons (utilisation du bouton poussoir)
    def motion_sensor(self):
        buttonvalue = GPIO.input(self.pin)

        if buttonvalue != self.PreValue:
            while not buttonvalue == 0:
                buttonvalue = GPIO.input(self.pin)
            return "button pressed"

    # IN : le dictionnaires de valeur GEN (voir CONFIG.py)
    # Modifie la valeurs "actuel" dans le dictionnaires de valeur GEN
    def dictionary_modification(self, gen):
        pas_max = gen["long"]

        if self.name == "bouton_PREV":
            if gen["actuel"][0] < pas_max:
                gen["actuel"][0] += 1

        elif self.name == "bouton_NEXT":
            if gen["actuel"][0] > 0:
                gen["actuel"][0] -= 1

        return gen

# Crée une liste d'objet button et configure chaque canal comme entrée ou sortie pour les boutons
button_list = []
for button_name in Bouton.keys():
    PIN = Bouton[button_name]
    GPIO.setup(PIN, GPIO.IN)
    button = Bouton(button_name, PIN)
    button_list.append(button)

# Crée une liste d'objet encoder et configure chaque canal comme entrée ou sortie pour les encodeurs
encoder_list = []
for encoder_name in Encodeur.keys():
    CLK = Encodeur[encoder_name][0]
    DT = Encodeur[encoder_name][1]
    SW = Encodeur[encoder_name][2]
    GPIO.setup(CLK, GPIO.IN)
    GPIO.setup(DT, GPIO.IN)
    if SW is not None:
        GPIO.setup(SW, GPIO.IN)
    encoder = Encoder(encoder_name, CLK, DT, SW)
    encoder_list.append(encoder)

# Boucle
while True:
    for encoder in encoder_list:
        if encoder.motion_sensor() == "button pressed":
            GEN, SEQ = encoder.dictionary_modification(None, GEN, SEQ)

        elif encoder.motion_sensor() == "rotated clockwise":
            GEN, SEQ = encoder.dictionary_modification("+", GEN, SEQ)

        elif encoder.motion_sensor() == "rotated counter-clockwise":
            GEN, SEQ = encoder.dictionary_modification("-", GEN, SEQ)

    for button in button_list:
        if button.motion_sensor() == "button pressed":
            GEN = button.dictionary_modification(GEN)
