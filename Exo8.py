#Exercice 1

#Transformer "Au clair de la lune" en "Au clair du soleil" (en chaînant replace())

base = "Au clair de la lune"
resultat = base.replace("de la lune", "du soleil")

print(resultat)

#Exercice 2

#Compter le nombre de 'e' dans la phrase

phrase = "J'aime bien le python même si le snake case, ça fait bizarre au début"
nombre_e = phrase.count("e")

print(nombre_e)

#Exercice 3

#Transformer la phrase en une seule ligne de code
#Résultat attendu : "Python c'est trop cool"

phrase = " python\tc'est\ntrop cool xx"
print(phrase.strip().replace("\t", " ").replace("\n", " ").replace(" xx", "").capitalize())

#Exercice 4

#Compter le nombre de phrases dans le texte

texte_super_interessant = """L'ornithorynque ne peut être confondu avec aucun
autre animal. C'est un petit mammifère – il dépasse rarement 2 kg – vraiment
original, à la fourrure courte et dense et au large bec de canard.
Son pelage est typique d'une espèce aquatique. La peau est protégée par une dense
couche de poils de bourre, qui maintiennent une pellicule d'air tempéré entre elle
et l'eau. Les poils de jarre, plus longs, protègent l'ensemble. La fourrure est
presque aussi dense sur le ventre que sur le dos. Seule la couleur change.
"""

nombre_phrases = texte_super_interessant.count(".")
print(nombre_phrases)