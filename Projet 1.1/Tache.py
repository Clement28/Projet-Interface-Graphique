class Tache:
    
    def __init__(self, nom, liste_operation):
        self.nom = nom
        self.liste_operation = liste_operation
        self.dep = []
        
    def deplacement(self, dep):
        self.dep = dep    