# -*- coding: utf-8 -*-

import kivy
kivy.require('1.7.2')

from Atelier import *
from Navette import *
from Operation import *
from Poste import *
from Tache import *
from gen_chemin import *

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from functools import partial

class CustomPopup(Popup):
    pass

class SampleBox(BoxLayout):
    pass

#Ajout de la liste des opérations (switch et label) sur le Bouton sélectionné
def add_op_poste_box(box, op_list):
    for i in range(len(op_list)):
        label = Label(text = op_list[i].nom)
        box.add_widget(label)
        box.add_widget(Switch(id = label.text, active = op_list[i].status)) 

#Trouver le nom de l'opération passé en argument retourne l'objet opération        
def trouverOperation(poste,nom):
    for i in poste.liste_operation_base:
        if i.nom == nom:
            return i
            break

#Mise à jour des opérations du poste concerné
def maj_poste_operation_status(poste):
    for i in range (1,len(poste.box_poste.children),2):
        nom = poste.box_poste.children[i].id
        operation = trouverOperation(poste,nom)
        operation.status = poste.box_poste.children[i].active
        if operation.status == False and operation in poste.liste_operation_effective:
            poste.supp(operation)
        if operation.status == True and\
        operation not in poste.liste_operation_effective:
            poste.ajout(operation)
    
class Poste:
    nombreOperationBase = 0
    nombreOperationEffective = 0

    #Initialisation du poste avec le nom en argument
    def __init__(self, nom):
        self.nom = nom
        self.liste_operation_base = []
        self.liste_operation_effective = []
    
    #Ajout d'une opération à un poste
    def ajout(self, operation):
        if operation not in self.liste_operation_base:
            self.liste_operation_base.append(operation)
            self.nombreOperationBase +=1
        if operation not in self.liste_operation_effective:    
            self.liste_operation_effective.append(operation)
            self.nombreOperationEffective +=1
        else:
            print "L'opération n'a pas pu être ajoutée car elle existe déja"    
    
    #Suppression d'une opération à un poste    
    def supp(self, operation):
        if operation in self.liste_operation_effective:
            self.liste_operation_effective.remove(operation)
            self.nombreOperationEffective -=1
        else:
            print "L'opération n'a pas pu être enlevée car elle n'existe pas"
    
    #Retourne une Alerte sur le poste concerné : 
    #[0 = RAS // 1 = Au moins une opération HS // 2 = Tous les opérations HS] 
    #-1 En cas d'erreur
    def NiveauAlerte(self):
        if (self.nombreOperationBase == self.nombreOperationEffective):
            return 0
            
        elif (self.nombreOperationBase > self.nombreOperationEffective >= 1):
            return 1   
            
        elif (self.nombreOperationEffective == 0):
            return 2
            
        else:
            return -1
         
    #Génération de la Popup sur le poste concerné     
    def maPopup(self):
        self.box_poste = SampleBox(orientation = "vertical")
        self.popup_poste = CustomPopup(size_hint=(.3, .7), auto_dismiss=False)
        self.popup_poste.add_widget(self.box_poste)
        add_op_poste_box(self.box_poste, self.liste_operation_base)
        bouton = Button(text = "Fermer et sauvegarder")
        bouton.bind(on_press=partial(self.appuieBoutonPoste, self, self.popup_poste))
        self.box_poste.add_widget(bouton)
    
    #Mise à jour des opérations du poste par appuie sur le bouton     
    def appuieBoutonPoste(instance, poste, popup, *args):
        maj_poste_operation_status(poste)
        args[0].on_press = popup.dismiss
        print poste.NiveauAlerte()