#Programme pour avoir des stats sur un fichier texte
def charger_fichier(nomfichier):
    nomdufichier = nomfichier
    nblignes = 0
    nbmots = 0
    compteur = {}
    try:
        #Ouverture du fichier
        with open(f"exercice-5/{nomdufichier}","r") as fichier:
            #Comptage des lignes + affichage de celles-ci
            for ligne in fichier:
                ligne = ligne.strip()
                nblignes += 1
                print(ligne)

                #Séparation et comptage des mots dans la chaine mots(tt les mots de la ligne)
                mots = ligne.split()
                nbmots += len(mots)

                #Comptage de chaque mots dans chaque ligne
                for mot in mots:
                    if mot in compteur:
                        compteur[mot] +=1


                        
                print(mots)
                nbmots +=1
            print(f"Il y a {nbmots} mots dans ce texte.")
            print(f"Il y a {nblignes} lignes dans ce texte.")
            print(f"Le mot le plus fréquent est {mot_frequent}")
    except FileNotFoundError:
        pass
    return fichier


            





nomfichier = input("Entre le nom du fichier : ")
charger_fichier(nomfichier)
