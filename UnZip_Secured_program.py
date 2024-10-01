import zipfile
import os
import subprocess
import sys

def is_within_directory(directory, target):
    #Fonction qui verifie que le chemin entre le répertoire et la cible est là même
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)
    return os.path.commonpath([abs_directory]) == os.path.commonpath([abs_directory, abs_target])

def unzip_secure_with_check(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.infolist():
            extracted_path = os.path.join(extract_path, member.filename)
            if not is_within_directory(extract_path, extracted_path):
                print(f"Extraction bloquée pour {member.filename} : tentative de Zip Slip détectée")
            else:
                zip_ref.extract(member, extract_path)

    # Vérifier si le script malicious.sh a été extrait
    malicious_script_path = os.path.join(extract_path, 'malicious.sh')
    if os.path.exists(malicious_script_path):
        print(f"Script malveillant détecté : {malicious_script_path}")
        print("Exécution bloquée du script malveillant")

unzip_secure_with_check(sys.argv[1], 'secure_unzipped')
print("Extraction sécurisée terminée")
