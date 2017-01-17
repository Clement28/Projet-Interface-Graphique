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
    popup_prod=CustomPopup(size_hint=(.6, .3), auto_dismiss=True)
    popup_prod.add_widget(box_prod)
    
    
            
    for i in atelier.liste_poste:
        i.maPopup()
    
    
    def set_title_poste(self, nom_poste):
        
        
        self.po = trouverPoste(self.atelier,nom_poste)
        self.po.popup_poste.title = "Operations du "+nom_poste
        self.po.popup_poste.open()
        
        
    def set_title_prod(self, nom_prod):
        
        self.popup_prod.title = "Avancement de la prod: "+prod
        self.popup_prod.open()    
        
        
#------------------------------------------------------------------------------        
    


















class gridlayoutapp(App):
    time=time.time()
    def build(self):
        return SampleGridLayout()
         
         

glApp = gridlayoutapp()

glApp.run()