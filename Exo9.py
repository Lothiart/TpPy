import math

# ==============================
# Exercice 1 : Calculs de base
# ==============================

# 1. Calculez la somme de 15 et 23
print(15 + 23)  # Résultat : 38

# 2. Soustrayez 42 de 57
print(57 - 42)  # Résultat : 15

# 3. Multipliez 6 par 9
print(6 * 9)  # Résultat : 54

# 4. Divisez 100 par 25
print(100 / 25)  # Résultat : 4.0

# 5. Trouvez le reste de la division de 29 par 5
print(29 % 5)  # Résultat : 4

# 6. Effectuez une division entière de 29 par 5
print(29 // 5)  # Résultat : 5

# 7. Calculez 2 à la puissance de 10
print(2 ** 10)  # Résultat : 1024


# ==========================================
# Exercice 2 : Opérateurs avancés (math)
# ==========================================

# 1. Calculez la racine carrée de 81
print(math.sqrt(81))  # Résultat : 9.0

# 2. Arrondissez 7.8 à l'entier inférieur
print(math.floor(7.8))  # Résultat : 7

# 3. Arrondissez 7.2 à l'entier supérieur
print(math.ceil(7.2))  # Résultat : 8


# =================================
# Exercice 3 : Opérateurs d'assignation
# =================================

# 1. Initialisez a à 10 puis ajoutez 5
a = 10
a += 5
print(a)  # Résultat : 15

# 2. Initialisez b à 20 puis soustrayez 7
b = 20
b -= 7
print(b)  # Résultat : 13

# 3. Initialisez c à 3 puis multipliez par 4
c = 3
c *= 4
print(c)  # Résultat : 12

# 4. Initialisez d à 50 puis divisez par 2
d = 50
d /= 2
print(d)  # Résultat : 25.0

# 5. Initialisez e à 9 puis calculez le reste de la division par 4
e = 9
e %= 4
print(e)  # Résultat : 1


# =================================
# Exercice 4 : Opérateurs de comparaison
# =================================

# 1. Vérifiez si 15 est supérieur à 10
print(15 > 10)  # Résultat : True

# 2. Vérifiez si 8 est inférieur ou égal à 8
print(8 <= 8)  # Résultat : True

# 3. Vérifiez si 20 est égal à 25
print(20 == 25)  # Résultat : False

# 4. Vérifiez si 30 est différent de 30
print(30 != 30)  # Résultat : False

# 5. Vérifiez si "Bonjour" est identique à "bonjour"
print("Bonjour" == "bonjour")  # Résultat : False


# =================================
# Exercice 5 : Opérateur d'appartenance
# =================================

# 1. Vérifiez si 'a' est présent dans "programmation"
print('a' in "programmation")  # Résultat : True

# 2. Vérifiez si "Python" est présent dans la phrase
print("Python" in "Le Python est un langage génial")  # Résultat : True

# 3. Vérifiez si le nombre 5 est dans la liste
print(5 in [1, 2, 3, 4, 6])  # Résultat : False

# 4. Vérifiez si 'z' est absent de "éducation"
print('z' not in "éducation")  # Résultat : True

# 5. Vérifiez si 10 n'est pas dans la liste
print(10 not in [2, 4, 6, 8])  # Résultat : True
