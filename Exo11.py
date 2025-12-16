
# Exercice 1
# Demander à l'utilisateur de taper un nombre
# Si celui-ci est pair, printer "Vous avez entré un nombre pair."
# Si celui-ci est impair, printer "Vous avez entré un nombre impair."
# Si l'information entrée n'est pas un nombre
# printer "Vous devez entrer un nombre!"


valeur = input("Entrez un nombre : ")

if valeur.isdigit():
    nombre = int(valeur)
    if nombre % 2 == 0:
        print("Vous avez entré un nombre pair.")
    else:
        print("Vous avez entré un nombre impair.")
else:
    print("Vous devez entrer un nombre!")


# Exercice 2
# Demander à un utilisateur de taper un mot
# Si celui-ci possède la lettre e OU la lettre a printer "Beep"
# Si celui-ci possède la lettre e OU la lettre a,
# mais sans que les deux conditions soient vraies en même temps,
# printer "Boop"

mot = input("Entrez un mot : ").lower()

contient_e = 'e' in mot
contient_a = 'a' in mot

if contient_e or contient_a:
    if contient_e != contient_a:
        print("Boop")
    else:
        print("Beep")


# Exercice 3 (OPTIONNEL)
# A l'aide d'un match case et d'une boucle :
# - printer "RGB" si la couleur est au format RGB
# - printer "RGBA" si la couleur est au format RGBA
# - si r, g, b == 0 et alpha > 0 (si existant) :
#   printer "Couleur noire" en priorité
# - si r, g, b == 255 et alpha > 0 (si existant) :
#   printer "Couleur blanche" en priorité
#
# Résultat attendu :
# RGB RGBA RGB de couleur noire RGBA RGBA
# RGBA de couleur blanche RGBA

colors = [
    (12, 72, 89),
    (23, 77, 200, 1),
    (0, 0, 0),
    (123, 123, 67, 1),
    (255, 255, 255, 0),
    (255, 255, 255, 1),
    (0, 0, 0, 0)
]

for color in colors:
    match color:

        # Format RGB
        case (r, g, b):
            if r == g == b == 0:
                print("RGB de couleur noire")
            elif r == g == b == 255:
                print("RGB de couleur blanche")
            else:
                print("RGB")

        # Format RGBA
        case (r, g, b, a):
            if a > 0 and r == g == b == 0:
                print("RGBA de couleur noire")
            elif a > 0 and r == g == b == 255:
                print("RGBA de couleur blanche")
            else:
                print("RGBA")
