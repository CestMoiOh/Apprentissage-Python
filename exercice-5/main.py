def charger_fichier(nomfichier):
    nomdufichier = nomfichier
    try:
        with open(f"exercice-5/{nomdufichier}","r") as fichier:
            for ligne in fichier:
                print(ligne)
            for mots in fichier:
                print(mots)
    except FileNotFoundError:
        pass
    return fichier


            





nomfichier = input("Entre le nom du fichier : ")
charger_fichier(nomfichier)
