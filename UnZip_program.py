import zipfile
import os
import subprocess
import sys

def unzip_and_execute(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    
    # Vérifier si un script malveillant a été extrait et l'exécuter
    malicious_script_path = os.path.join(extract_path, 'malicious.sh')
    if os.path.exists(malicious_script_path):
        print(f"Exécution du script malveillant : {malicious_script_path}")
        subprocess.run([malicious_script_path], shell=True)

# Exemple d'utilisation
unzip_and_execute(sys.argv[1], '.prank')
print("Extraction non sécurisée avec exécution terminée")