
#liste des fichiers dans le dossier /dossierRempli

import glob
import pathlib
from pathlib import Path

import win32com.client as win32

import pythoncom
import ctypes
import os


# watchdog
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from utils.loadConfig import loadConfig

# recovery saved path
tempdir = loadConfig()
# fonction qui supprime les fichiers d'un dossier
def EraseFile(folder):
    try:
        files=os.listdir(folder)
        for i in range(0,len(files)):
            os.remove(folder+'/'+files[i])
    except:
        print('problem')
        ctypes.windll.user32.MessageBoxW(0, "Seulement des fichiers sont accepté","fichiers seulement",1)

def on_created(event):
    print("created")
    files = []
    filesAbsolute = []
    #target path
    pathFolder= tempdir
    

    for file in glob.glob(tempdir+"*/*"):
        files.append(file)


    for file in files:
        filesAbsolute.append(Path(file).resolve())

    for file in filesAbsolute:
        file = str(file) 
        print(file)   
        

    pythoncom.CoInitialize()

    # Genere l'email via compte outlook local


    outlook = win32.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)
    mail.Display()

    
    #mail.To = 'To address'
    #mail.Subject = 'Message subject'
    #mail.Body = 'Message body'
    #mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

    # To attach a file to the email (optional):
    #attachment  = "Path to the attachment"
    #mail.Attachments.Add("dossierRempli\pli.txt")

    
    for file in filesAbsolute:
        try:
            mail.Attachments.Add(str(file))
        except:
            print('problem')
            ctypes.windll.user32.MessageBoxW(0, "Seulement des fichiers sont accepté","fichiers seulement",0)
        

    #while not mail.sent :
     #       print('pas envoyé')
       #     print(mail.sent)
       #     time.sleep(2)
    try:

        while  not mail.sent :
                print('pas envoyé')
                time.sleep(2)
    except :
        print('envoyé')
        EraseFile(pathFolder)
    else:
        print("envoyé2")

   
    
            
    
       #for file in glob.glob("dossierRempli/*"):
            #os.remove(file)



      

def on_moved(event):
    print("moved")



#from threading import Timer
if __name__ == "__main__":
    
    event_handler = FileSystemEventHandler()

    #calling functions
    event_handler.on_created = on_created
    event_handler.on_moved = on_moved

    path=tempdir
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()
    try:
        print("Surveillance")
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        print('done')
    observer.join()

