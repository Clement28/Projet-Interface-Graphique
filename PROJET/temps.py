# -*- coding: utf-8 -*-

import time
import datetime
import signal
import sys

debut = time.time()

time.sleep(0)

fin = time.time()

print fin-debut

print time.localtime()
print time.localtime(fin-debut)

print time.strftime("%A %d %B %Y %H:%M:%S")

#POUR MOINS DE PRECISIONS mais écrire la date un peu mieux
date = datetime.date(2010, 12, 25)
print date

#RENVOIE DATE AUJOURDHUI
print datetime.date.today()

#DATE CORRESPONDANT AU TEMPS PASSE EN ARGUMENT
print datetime.date.fromtimestamp(1233561615)

#Date et heure actuelle
print datetime.datetime.now()

#Heure actuelle (heures, min, seconde, micro secondes, fuseau horaires)
heure = datetime.time(1, 15)
print datetime.time(5, 15, 32, 256)

def fermer_programme(signal, frame):
    print("C'est l'heure de la fermeture !")
    sys.exit(0)

# Connexion du signal à notre fonction
signal.signal(signal.SIGINT, fermer_programme)

print("Le programme va boucler...")
debut = time.time()
while True:
    fin = time.time()
    if (fin - debut >= 2):
        print ("Ca fait deux secondes !!")
        debut = time.time()
    continue

