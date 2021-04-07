import pickle
import os.path

saveFileInit = "../saveFile/saveCg.txt"

#Ouverture du fichier si il existe et récupération de la liste
if os.path.isfile(saveFileInit):
    saveFile = open(saveFileInit,"rb")
    variables = pickle.load(saveFile)
    saveFile.close()

    #Affichage de la liste
    print(variables)

    
else:
    #Le fichier n'existe pas
    print("Fichier " + fichierini + " non trouvé")



####################
"""
fichierini = "diaporamaini"

#Ouverture du fichier si il existe et récupération de la liste
if os.path.isfile(fichierini):
    fichierSauvegarde = open(fichierini,"rb")
    variables = pickle.load(fichierSauvegarde)
    fichierSauvegarde.close()

    #Affichage de la liste
    print(variables)

    #récupération des données dans les variables
    serveursmb = variables[0]
    partagesmb = variables[1]
    utilisateur = variables[2]
    mot_de_passe = variables[3]
    domaine = variables[4]
    fichier_diaporama = variables[5]

    #Affichage des variables
    print("Serveur : ", serveursmb)
    print("Partage : ", partagesmb) 
    print("Utilisateur : ",utilisateur)
    print("Mot de passe : ", mot_de_passe)
    print("Domaine : ", domaine)
    print("Fichier du diaporama : ", fichier_diaporama)
else:
    #Le fichier n'existe pas
    print("Fichier " + fichierini + " non trouvé")
    """