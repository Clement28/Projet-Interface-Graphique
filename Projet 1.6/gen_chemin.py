# -*- coding: utf-8 -*-

def solutionTache(Tache,listePoste) :
    tab_final = []
    for i in Tache:
        tab = []
        for j in range(len(listePoste)):
            for k in listePoste[j].liste_operation_effective:	
                if i == k:
                    tab.append(listePoste[j].nom)
                    
        tab_final.append(tab)

    return tab_final


#DONNE LES POSTES POUR LESQUELS ON PEUT FAIRE LES TACHES PAR ORDRE DAPPARITION DES TACHES
##PAR EXEMPLE POUR TACHE 0 ON A LES POSTES 0 ET 1 de dispo

##
###RENVOIE LE CHEMIN DU CHIFFRE VERS LES ELEMENTS DE LA LISTE
def choixUnique(posteDepart,postesArrivee):
    solution=[[]]
    #ajoute en premier lieu le chiffre dans la liste
    for i in range(len(postesArrivee)) :
        if type(posteDepart) == str:
            solution[i].append(posteDepart)
            solution.append([])
        else:
            for l in range(len(posteDepart)):
                solution[i].append(posteDepart[l])
            solution.append([])
    solution.remove([])
    cpt = 0
    #ajoute en second lieu les autres chiffres dans la liste
    for j in range(len(postesArrivee)):
        solution[cpt].append(postesArrivee[j])
        cpt += 1
    return solution
    

##    

##
def cheminSolution(Tache,listePoste):
    solutionFINALE = []
    Etats = solutionTache(Tache, listePoste)
    if Etats == [[]]:
        print "Pas de solution"
    else:
        etatInitial = Etats[0]
        Etats.remove(Etats[0])
        autresEtats = Etats
        liste_solution = []
        for i in range(len(etatInitial)):
            solution = choixUnique(etatInitial[i],autresEtats[0])
            liste_solution.append(solution)
            
        for m in range(1,len(autresEtats)):
            for i in range(len(liste_solution)):
                for j in range(len(liste_solution[i])):
        
                    test = choixUnique(liste_solution[i][j],autresEtats[m])
                    liste_solution.append(test)
                
        tailleMax = len(liste_solution[len(liste_solution)-1][0])
        
        for i in range(len(liste_solution)):
            for j in range(len(liste_solution[i])):
                if len(liste_solution[i][j]) == tailleMax:
                    solutionFINALE.append(liste_solution[i][j])
                
    
                
    return solutionFINALE

