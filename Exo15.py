# Exercice 1 : Création et conversion de tuples
# 1. Créez un tuple avec les éléments suivants : 10, 20, 30, 40. Affichez ce tuple.
# 2. Convertissez ce tuple en une liste, puis affichez cette liste.
# 3. Modifiez le premier élément de la liste pour qu'il soit égal à 15, puis affichez la liste.
# 4. Convertissez la liste modifiée en un nouveau tuple, puis affichez ce nouveau tuple.

# 1.
t = (10, 20, 30, 40)
print(t)

# 2.
liste = list(t)
print(liste)

# 3.
liste[0] = 15
print(liste)

# 4.
nouveau_tuple = tuple(liste)
print(nouveau_tuple)

# Exercice 2 : Accès et modification indirecte
# 1. Créez un tuple contenant une chaîne de caractères, un nombre, et une liste. 
# Affichez ce tuple.
# 2. Accédez au troisième élément du tuple (la liste) et modifiez son premier élément pour qu'il soit égal à 10. Affichez le tuple.
# 3. Essayez de modifier le deuxième élément du tuple directement pour qu'il soit égal à 200. Que se passe-t-il ?


# 1.
t = ("Python", 42, [1, 2, 3])
print(t)

# 2.
t[2][0] = 10
print(t)

# 3.
#t[1] = 200
#TypeError: 'tuple' object does not support item assignment


# OPTIONNEL Exercice 3 : Utilisation des tuples pour les performances
# 1. Créez un tuple contenant les nombres de 1 à 1_000_000. Utilisez la fonction range() pour vous aider.
# 2. DEFI : Comparez le temps de création d'un tuple et d'une liste contenant les mêmes éléments en utilisant la fonction time de la bibliothèque time.
# Note: Les résultats de temps peuvent varier en fonction de l'environnement d'exécution
import time

# 1.
start = time.time()
t = tuple(range(1, 1_000_001))
end = time.time()
print("tuple :", end - start)

# 2.
start = time.time()
l = list(range(1, 1_000_001))
end = time.time()
print("liste :", end - start)
