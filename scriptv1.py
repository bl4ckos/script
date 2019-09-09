#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,shutil

total, used, free = shutil.disk_usage("etc/wordpress, etc/apache")

("Total: %d GB" % (total // (2**30)))
("Used: %d GB" % (used // (2**30)))
("Free: %d GB" % (free // (2**30)))

if disk > Free: print("espace disponible")
else:
	print("impossible de faire la sauvegarde")
	sys.exit(1) 


#		compresser les dossiers apache et wordpress ( complète en week end et incremental en semaine )
import tarfile

/etc/apache2 

# faire un fichier tar avec le meme nom et la date du jour pour differentier les tar
joindre la date et l'heure au nom du fichier tar 
#  En SSH transférer le fichier TAR sur serveur distant dans un dossier a la racine

with pysftp.Connection('ip', username='login', password='password') as sftp: 
    with sftp.cd('/path/to/upload'):
        sftp.put('path/to/file')

# Supprimer les vieux fichiers de 3 semaines d'intervalle 

import os
import time

current_time = time.time()

for f in os.listdir():
    creation_time = os.path.getctime(f)
    if (current_time - creation_time) // (24 * 3600) >= 7:
        os.unlink(f)
        print('{} removed'.format(f))

# notifier le bon déroulement de l'intervention du script à chaque sauvegarde
create log dans /etc/logbackup ok date ok





# 									script sur serveur distant à lancer soi même si besoin

# liste les fichiers tar du dossier à la racine

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# choisir le fichier à extraire

user_answer = input("choisisez le fichier a extraire")

###	- extraire le fichier - ####
import tarfile
tar = tarfile.open("sample.tar.gz")
tar.extractall(./)
tar.close()

# transfert le fichier extrait sur mon serveur principal

with pysftp.Connection('ip', username='login', password='password') as sftp: 
    with sftp.cd('/path/to/upload'):
        sftp.put('path/to/file')

# retour de commande transfert ok
Print if: