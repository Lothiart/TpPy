from datetime import date

prenom = "bobby"
age = 30
date_naissance = date(1992, 5, 26)

phrase = (
    f"Bonjour, je m'appelle {prenom.capitalize()}, "
    f"j'ai {age:04d} ans, "
    f"je suis né le {date_naissance.strftime('%B %d %Y')}."
)

print(phrase)
