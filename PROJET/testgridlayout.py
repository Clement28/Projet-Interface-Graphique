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


class CustomPopup(Popup):
    pass
            
            
class SampleBox(BoxLayout):
    pass


def add_op_poste_box(box, op_list):
    
    for i in range(len(op_list)):
        label = Label(text = op_list[i].nom)
        box.add_widget(label)
        box.add_widget(Switch(id = label.text, active = op_list[i].status))    
        
def trouverPoste(atelier,nom):
    for i in atelier.liste_poste:
        if i.nom == nom:
            return i
            break
    
            
              

class SampleGridLayout(GridLayout): 
        
        
#------------------------------------------------------------------------------
        
    op1 = Operation('soudure')
    op2 = Operation('peinture')
    op3 = Operation('assemblage')
    op4 = Operation('Detruire')



    po1 = Poste('Poste 1')
    po2 = Poste("Poste 2")
    po3 = Poste("Poste 3")
    po4 = Poste("Poste 4")
    po5 = Poste("Poste 5")

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
        
#------------------------------------------------------------------------------        
    
    box_prod = SampleBox(orientation = "vertical")
    box_Nav = SampleBox(orientation = "vertical")
    
    pb = ProgressBar()
    lab = Label()
    box_prod.add_widget(lab)
    box_prod.add_widget(pb)
    
    box_poste1 = SampleBox(orientation = "vertical")
    popup_poste1 = CustomPopup(size_hint=(.3, .7), pos=(10, 10))
    box_poste2 = SampleBox(orientation = "vertical")
    popup_poste2 = CustomPopup(size_hint=(.3, .7), pos=(10, 10))
    box_poste3 = SampleBox(orientation = "vertical")
    popup_poste3 = CustomPopup(size_hint=(.3, .7), pos=(10, 10))
    
    i = trouverPoste(atelier, "Poste 1")
    test = i.liste_operation_base
    print test
    add_op_poste_box(box_poste1, test)
    
    i = trouverPoste(atelier, "Poste 2")
    test = i.liste_operation_base
    print test
    add_op_poste_box(box_poste2, test)
    
    i = trouverPoste(atelier, "Poste 3")
    test = i.liste_operation_base
    print test
    add_op_poste_box(box_poste3, test)
    
    popup_poste1.add_widget(box_poste1)
    popup_poste1.auto_dismiss = True
    popup_poste2.add_widget(box_poste2)
    popup_poste2.auto_dismiss = True   
    popup_poste3.add_widget(box_poste3)
    popup_poste3.auto_dismiss = True   
  
    popup_prod = CustomPopup(size_hint=(.7, .4), pos=(10, 10))
    popup_prod.add_widget(box_prod)
    popup_prod.auto_dismiss = True
        
             
        
    def set_title_poste1(self, nom_poste):
    
        self.popup_poste1.title = "Operations du "+nom_poste
        self.popup_poste1.open()
        
    def set_title_poste2(self, nom_poste):
    
        self.popup_poste2.title = "Operations du "+nom_poste
        self.popup_poste2.open()  
        
    def set_title_poste3(self, nom_poste):
    
        self.popup_poste3.title = "Operations du "+nom_poste
        self.popup_poste3.open()    
        
        
       
        
    def set_title_prod(self, nom_poste):
        
        self.popup_prod.title = "Avancement de la prod: "+nom_poste
        self.popup_prod.open()    
        
        
#------------------------------------------------------------------------------        
    


















class gridlayoutapp(App):
    time=time.time()
    def build(self):
        return SampleGridLayout()
         
         

glApp = gridlayoutapp()

glApp.run()