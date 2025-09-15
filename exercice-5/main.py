def charger_fichier(nomfichier):
    nomdufichier = nomfichier
    nblignes = 0
    nbmots = 0
    try:
        with open(f"exercice-5/{nomdufichier}","r") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                nblignes += 1
                print(ligne)

                mots = ligne.split()
                nbmots += len(mots)
                print(mots)
                nbmots +=1
            print(f"Il y a {nbmots} mots dans ce texte.")
            print(f"Il y a {nblignes} lignes dans ce texte.")
    except FileNotFoundError:
        pass
    return fichier


            





nomfichier = input("Entre le nom du fichier : ")
charger_fichier(nomfichier)
