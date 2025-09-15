#Fonction pour charger la liste
def charger_taches():
    taches = []
    try:
        with open("exercice-4/list.txt", "r") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:
                    if "|" in ligne:
                        statut_str, nom_tache = ligne.split("|", 1)
                        statut = statut_str == "1"
                        taches.append([nom_tache, statut])
                    else:
                        taches.append([ligne, False])
    except FileNotFoundError:
        pass
    return taches

#Fonction pour sauvegarder la liste
def sauvegarder_taches(taches):
    with open("exercice-4/list.txt","w") as fichier:
        for tache in taches:
            nom_tache = tache[0]
            statut = "1" if tache[1] else "0"
            fichier.write(f"{statut}|{nom_tache}\n")

#Fonction pour afficher les tâches
def afficher_taches(taches):
    print("\n--- VOS TÂCHES ---")
    for i, tache in enumerate(taches):
        nom = tache[0]
        terminée = tache[1]
        statut = "✓" if terminée else "☐"
        print(f"{i+1}. [{statut}] {nom}")
    print("------------------\n")

#Fonction d'ajout d'une tâche
def ajout_tache(taches):
    tacheajout = input("Entrez la tâche à ajouter : ")
    taches.append([tacheajout, False])
    print(f"Tâche {tacheajout} ajoutée avec succès !")

#Fonction de suppression d'une tâche
def suppr_tache(taches):
    afficher_taches(taches)
    numéro = int(input("Numéro de la tâche à supprimer : "))-1
    del taches[numéro]
    print(f"La tâche numéro : {numéro+1} à été supprimé avec succès !")

#Fonction pour marquer une tâche comme terminé
def marqué_terminé(taches):
    afficher_taches(taches)
    try:
        numéro = int(input("Numéro de la tâche à cocher terminé : "))-1
        if 0 <= numéro < len(taches):
            taches[numéro][1] = True
            print(f"Tâche {taches[numéro][0]} marquée comme terminée !")
        else:
            print("Numéro invalide !")
    except ValueError:
        print("Erreur : Entrez un nombre !")





#Affichage de l'interface
taches = charger_taches()
while True:
    choix = int(input("--- MA LISTE DE TACHES ---\n1. Afficher les tâches\n2. Ajouter une tâche\n3. Supprimer une tâche\n4. Marquer une tâche terminé\n5. Quitter\nTon choix : "))
    match choix:
        case 1:
            afficher_taches(taches)
        case 2:
            ajout_tache(taches)
            sauvegarder_taches(taches)
        case 3:
            suppr_tache(taches)
            sauvegarder_taches(taches)
        case 4:
            marqué_terminé(taches)
            sauvegarder_taches(taches)
        case 5:
            break