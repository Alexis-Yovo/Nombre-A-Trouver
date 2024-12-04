import random

# Génération du nombre aléatoire à deviner
nombre_a_deviner = random.randint(1, 10)

# Affichage des instructions pour l'utilisateur
print("J'ai choisi un nombre entier entre 1 et 10.")
print("Vous avez deux essais pour le trouver.")

# Première tentative de l'utilisateur
a = int(input("Première tentative : "))

# Vérification et affichage si le nombre est correct lors de la première tentative
if a == nombre_a_deviner:
    print("Félicitations ! Vous avez deviné le nombre.")
else:
    # Indication si le nombre est plus grand ou plus petit
    if a < nombre_a_deviner:
        print("Le nombre à deviner est plus grand que", a)
    else:
        print("Le nombre à deviner est plus petit que", a)
    
    # Deuxième tentative de l'utilisateur
    b = int(input("Deuxième tentative : "))
    
    # Vérification et affichage si le nombre est correct lors de la deuxième tentative
    if b == nombre_a_deviner:
        print("Félicitations ! Vous avez deviné le nombre.")
    else:
        print("Désolé, vous n'avez pas deviné le nombre. Le nombre à trouver était", nombre_a_deviner)
