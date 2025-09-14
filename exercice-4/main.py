#Création d'une liste vide
taches = []

def afficher_taches(taches):
    print("\n--- VOS TÂCHES ---")
    for i, tache in enumerate(taches, start=1):
        print(f"{i}. {tache}")
    print("------------------\n")

def ajout_tache(taches):
    tacheajout = input("Entrez la tâche à ajouter : "),"Pas faite"
    taches.append(tacheajout)
    print(f"Tâche {tacheajout} ajoutée avec succès !")

def suppr_tache(taches):
    afficher_taches(taches)
    numéro = int(input("Numéro de la tâche à supprimer : "))-1
    del taches[numéro]
    print(f"La tâche numéro : {numéro+1} à été supprimé avec succès !")

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
while True:
    choix = int(input("--- MA LISTE DE TACHES ---\n1. Afficher les tâches\n2. Ajouter une tâche\n3. Supprimer une tâche\n4. Marquer une tâche terminé\n5. Quitter\nTon choix : "))
    match choix:
        case 1:
            afficher_taches(taches)
        case 2:
            ajout_tache(taches)
        case 3:
            suppr_tache(taches)
        case 4:
            marqué_terminé(taches)
        case 5:
            break