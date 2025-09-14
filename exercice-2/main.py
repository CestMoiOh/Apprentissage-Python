import random
# Déclaration de la variable aléatoire choisie 
nbatrouver=random.randint(1,100)
nbchoisi=0
nbtentativesrestantes = 0

# Demande du nombre de la difficulté voulu et Recherche du nombre 
while nbtentativesrestantes == 0:
    choix = input("Choix de la difficulté (easy, medium, hard): ")
    
    match choix:
        case "easy":
            nbtentativesrestantes = 20
        case "medium":
            nbtentativesrestantes = 13 
        case "hard":
            nbtentativesrestantes = 8 
        case _:
            print("Entrez une des options disponibles !")

while nbatrouver!=nbchoisi and nbtentativesrestantes!=0:
    nbchoisi = int(input("Entrez un nombre entre 1 et 100\n"))
    if nbchoisi>nbatrouver:
        print("Moins !")
    elif nbchoisi<nbatrouver:
        print("Plus !")
    nbtentativesrestantes-=1
    print("Nombre de tentative restantes : ",nbtentativesrestantes," !")

# Affichage du résultat
print("Bien joué, le nombre était bien : ",nbatrouver," !")