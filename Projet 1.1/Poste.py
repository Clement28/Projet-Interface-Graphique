# -*- coding: utf-8 -*-

import kivy
kivy.require('1.7.2')

from Atelier import *
from Navette import *
from Operation import *
from Poste import *
from Tache import *
from gen_chemin import *

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

def add_op_poste_box(box, op_list):
    
    for i in range(len(op_list)):
        label = Label(text = op_list[i].nom)
        box.add_widget(label)
        box.add_widget(Switch(id = label.text, active = op_list[i].status)) 
        print Switch.active
        


class CustomPopup(Popup):
    pass

class SampleBox(BoxLayout):
    pass

def trouverOperation(poste,nom):
    for i in poste.liste_operation_base:
        if i.nom == nom:
            return i
            break
class test ():
    print "gjogogo"  


def majStatusOperations(poste):
    for i in range (len(poste.box_poste.children),2):
        nom = poste.box_poste.children[i].id
        operation = trouverOperation(poste,nom)
        operation.status = poste.box_poste.children[i].active
        print operation.status, operation.active
    
class Poste:
    
    
    
    
    nombreOperationBase = 0
    nombreOperationEffective = 0
    def __init__(self, nom):
        self.nom = nom
        self.liste_operation_base = []
        self.liste_operation_effective = []

               
        
    def ajout(self, operation):
        if operation not in self.liste_operation_base:
            self.liste_operation_base.append(operation)
            self.nombreOperationBase +=1
        else:
            print "L'opération n'a pas pu être ajoutée car elle existe déja"
        if operation not in self.liste_operation_effective:    
            self.liste_operation_effective.append(operation)
            self.nombreOperationEffective +=1
        else:
            print "L'opération n'a pas pu être ajoutée car elle existe déja"    
        
    def supp(self, operation):
        if operation in self.liste_operation_effective:
            self.liste_operation_effective.remove(operation)
            self.nombreOperationEffective -=1
        else:
            print "L'opération n'a pas pu être enlevée car elle n'existe pas"
        
    def NiveauAlerte(self):
        
        
        if (self.nombreOperationBase == self.nombreOperationEffective):
            return 0
            
        elif (self.nombreOperationBase > self.nombreOperationEffective >= 1):
            return 1   
            
        elif (self.nombreOperationEffective == 0):
            return 2   
         
         
#    def test():
#            print "yes"
            
            
    def maPopup(self):
        
        print "pass1"
        self.box_poste = SampleBox(orientation = "vertical")
        self.popup_poste = CustomPopup(size_hint=(.3, .7), pos=(10, 10), auto_dismiss=False)
        self.popup_poste.add_widget(self.box_poste)
        add_op_poste_box(self.box_poste, self.liste_operation_base)
        self.box_poste.add_widget(Button(text = "Terminer !", on_press = test))
#       
        
        
        
        
 
        
        
            