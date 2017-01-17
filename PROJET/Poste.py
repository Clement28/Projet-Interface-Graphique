class Poste:
    
    nombreOperationBase = 0
    nombreOperationEffective = 0
    def __init__(self, nom):
        self.nom = nom
        self.liste_operation_base = []
        self.liste_operation_effective = []
             
                
        
    def ajout(self, operation):
        self.liste_operation_base.append(operation)
        self.liste_operation_effective.append(operation)
        self.nombreOperationBase +=1
        self.nombreOperationEffective +=1
        
    def supp(self, operation):
        self.liste_operation_effective.remove(operation)
        self.nombreOperationEffective -=1
        
    def NiveauAlerte(self):
        
        
        if (self.nombreOperationBase == self.nombreOperationEffective):
            return 0
            
        elif (self.nombreOperationBase > self.nombreOperationEffective >= 1):
            return 1   
            
        elif (self.nombreOperationEffective == 0):
            return 2        