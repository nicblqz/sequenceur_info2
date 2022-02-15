# dicos pour l'instant mais à changer en classes ?

PARAM1 = {"note":0, "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
PARAM2 = {"note":0, "gate":0, "cv1":0, "cv2":0, "cv3":0, "cv4":0}
# ...
SEQ = {"pas1":PARAM1, "pas2":PARAM2}

GEN = {"long":0, "bpm":0, "gamme":0}


# pins et autres (adapter avec le produit de philippe)

# Définit les pins utilisés par les encodeurs
Encodeur = {
    "encodeur_NOTE" : [5,6,None],
    "encodeur_GATE" : [0,11,None],
    "encodeur_CV1" : [20,21,None],
    "encodeur_CV2" : [12,16,None],
    "encodeur_CV3" : [8,7,None],
    "encodeur_CV4" : [24,25,None],
    "encodeur_PARAM" : [13,19,26]
    }

# Définit les valeurs initiales des encodeurs
val = [0,0,0,0,0,0,0]

# Définit les paliers en fonction des encodeurs
step = [int(4096/(12*5)),1,1,1,1,1,1]

# pDéfinit l'intervalle des encodeurs
interval = [(0,4096),(0,1),(0,4096),(0,4096),(0,4096),(0,4096),(0,4096)]

# Définit les pins utilisés par les Boutons
Bouton = {
    "bouton_PLAYPAS" : 10,
    "bouton_PLAY" : 22,
    "bouton_PREV" : 27,
    "bouton_NEXT" : 17,
        }

# écran
# pas les bonnes versions sur github
