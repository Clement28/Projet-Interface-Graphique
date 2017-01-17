# -*- coding: utf-8 -*-
import kivy
kivy.require('1.7.2')

from Atelier import *
from Navette import *
from Operation import *
from Poste import *
from Tache import *
from gen_chemin import *
from testgridlayout import *

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
import time




op1 = Operation('soudure')
op2 = Operation('peinture')
op3 = Operation('assemblage')
op4 = Operation('Detruire')



po1 = Poste('poste1')
po2 = Poste("poste2")
po3 = Poste("poste3")
po4 = Poste("poste4")
po5 = Poste("poste5")

t1 = Tache('t1', [op1.nom,op2.nom])
t2 = Tache('t2', [op1.nom,op3.nom])
t3 = Tache('t3', [op2.nom,op3.nom])
t4 = Tache('t4', [op4.nom])

po1.ajout(op1)
po1.ajout(op2)
po1.ajout(op3)

po2.ajout(op2)
po2.ajout(op3)

po3.ajout(op1)
po3.ajout(op3)


atelier = Atelier("ATELIER")
atelier.liste_poste = [po1,po2,po3,po4,po5]
atelier.liste_operation = [op1.nom, op2.nom, op3.nom]

print cheminSolution(t1.liste_operation, atelier.liste_poste)


nav1 = Navette('Navette1', t1)
nav2 = Navette('Navette1', t2)
nav3 = Navette('Navette1', t3)

nav1.Tache.deplacement(['poste1', 'poste1'])
print(nav1.Tache.dep)


po1.supp(op1)
po1.supp(op2)
po1.supp(op3)
print po1.NiveauAlerte()

#GENRATION DE TOUS LES CHEMINS POUR TOUTES LES NAVETTES
s1 = cheminSolution(t1.liste_operation, atelier.liste_poste)
s2 = cheminSolution(t2.liste_operation, atelier.liste_poste)
s3 = cheminSolution(t3.liste_operation, atelier.liste_poste)
s4 = cheminSolution(t4.liste_operation, atelier.liste_poste)

print "1", s1
print "2", s2
print "3", s3
print "4", s4

s2.remove(s2[1])

listeSol = [s1,s2,s3,s4]

def Unicite(solution):
    if len(solution) == 1:
        return True
    else:
        return False

print Unicite(s1)
print Unicite(s2)
print Unicite(s3)
print Unicite(s4)

listeChemin = []
for i in range(len(listeSol)):
    if len(listeSol[i]) == 0:
        print "Pas de solution !"
    elif Unicite(listeSol[i]) == True:
        listeChemin.append(listeSol[i][0])
        print listeChemin
        #print "UNI", listeSol
        for j in range(i+1,len(listeSol)):
            #print listeSol[j]
            if listeSol[i][0] in listeSol[j] and len(listeSol[j]) > 1:
                listeSol[j].remove(listeSol[i][0])
                print listeSol[j]
    else:
        
        listeChemin.append(listeSol[i])
        
print listeChemin











class gridlayoutapp(App):
    time=time.time()
    def build(self):
        return SampleGridLayout()
         
         

glApp = gridlayoutapp()

glApp.run()
        
