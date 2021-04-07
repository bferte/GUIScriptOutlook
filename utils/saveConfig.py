import pickle

tempdir = 'pfoo/gfdg/fdfgo'

def saveConfig() :
    folderTarget = tempdir
    saveFile = open("../saveFile/saveCg.txt","wb")
    pickle.dump(folderTarget, saveFile)
    saveFile.close()

saveConfig()


#Enregistrer mes variables sous forme d'une liste dans un fichier
#Initialisation des variables
#serveursmb = "PC-DOM"
#partagesmb = "Partage-Diaporama"
#utilisateur = "dominique"
#mot_de_passe = "motdepasse"
#domaine = "WORKGROUP"
#fichier_diaporama = "Diaporama.odp"

#Enregistrement des variables dans le fichier
#variables = [serveursmb, partagesmb, utilisateur, mot_de_passe, domaine, fichier_diaporama]
#fichierSauvegarde = open("diaporamaini","wb")
#pickle.dump(variables, fichierSauvegarde)
#fichierSauvegarde.close()