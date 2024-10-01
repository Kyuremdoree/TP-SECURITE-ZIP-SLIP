import zipfile
import os
import sys

# Créer un répertoire temporaire pour le fichier à zipper
os.makedirs('.evil', exist_ok=True)


#Chemin du programme
vulnerable_path = 'TODO'

# Créer un script Bash malveillant qui écrit un message dans le terminale
# que vous appelerez malicious.sh
TODO()

# Rendre le script exécutable

# Il faut mettre des droits d'exécution au fichier
TODO()

# Créer le fichier ZIP avec le script piégé
with zipfile.ZipFile(sys.argv[1], 'w') as zipf:
    zipf.write('.evil/'+vulnerable_path, arcname=vulnerable_path)

print("Fichier ZIP créé")