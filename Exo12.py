# Exercice 1
# Créer un script python écrivant 5 entiers aléatoires entre 0 et 100 dans un
# fichier .txt dans votre dossier 'Documents'
# Le résultat doit apparaître comme ceci: "Voici mes 5 nombres aléatoires: X, X,
# X, X et X"
# Printer le contenu du document
# Supprimer le fichier

import random
from pathlib import Path

documents_path = Path.home() / "Documents"
file_path = documents_path / "nombres_aleatoires.txt"

nombres = [random.randint(0, 100) for _ in range(5)]

texte = (
    f"Voici mes 5 nombres aléatoires: "
    f"{nombres[0]}, {nombres[1]}, {nombres[2]}, {nombres[3]} et {nombres[4]}"
)

file_path.write_text(texte, encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))
file_path.unlink()


# Exercice 2
# Avec l'aide du module datetime, printer l'âge de la personne possédant la date
# de naissance suivante
date_naissance = "1998-04-23"
# documentation Datetime

from datetime import datetime, date

date_naissance = datetime.strptime(date_naissance, "%Y-%m-%d").date()
aujourd_hui = date.today()

age = aujourd_hui.year - date_naissance.year
if (aujourd_hui.month, aujourd_hui.day) < (date_naissance.month, date_naissance.day):
    age -= 1

print(age)


# OPTIONNEL : Exercice 3
# A l'aide du module zipfile, extraire l'archives source.zip situé dans le dossier
# "Annexes"
# A l'aide du module pathlib, ou os, et d'une boucle, créer un trieur de fichier
# qui va répartir les fichiers extraits en 5 dossiers (Musique, Videos, Images,
# Documents, Divers) selon les règles suivantes
# 1. mp3, wav, flac : Musique
# 2. avi, mp4, gif : Videos
# 3. bmp, png, jpg : Images
# 4. txt, pptx, csv, xls, odp, pages : Documents
# 5. autres : Divers
# documentation ZipFile

import zipfile

annexes_path = Path("Annexes")
zip_path = annexes_path / "source.zip"
extract_path = annexes_path / "extracted"

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_path)

folders = {
    "Musique": ["mp3", "wav", "flac"],
    "Videos": ["avi", "mp4", "gif"],
    "Images": ["bmp", "png", "jpg"],
    "Documents": ["txt", "pptx", "csv", "xls", "odp", "pages"],
    "Divers": []
}

for folder in folders:
    (extract_path / folder).mkdir(exist_ok=True)

for file in extract_path.iterdir():
    if file.is_file():
        extension = file.suffix.lower().lstrip(".")
        moved = False

        for folder, extensions in folders.items():
            if extension in extensions:
                file.rename(extract_path / folder / file.name)
                moved = True
                break

        if not moved:
            file.rename(extract_path / "Divers" / file.name)
