import pickle
import os.path


def loadConfig():

    saveFileInit = "./saveFile/saveCg.txt"

    #Ouverture du fichier si il existe et récupération de la liste
    if os.path.isfile(saveFileInit):
        saveFile = open(saveFileInit,"rb")
        variables = pickle.load(saveFile)
        saveFile.close()

        #Affichage de la liste
        print(variables)
        return variables

        
    else:
        #File doesn't exist
        print("File " + saveFileInit + " not found")



