#Exercice n°3 : Créer une histoire avec des mots données. Compétences aprises, concaténation de chaine de caractères.
print ("Donne moi les mots qui te viennent en tête :\n")
lieu = input("Un lieu : ")
langue = input("Une langue : ")
animal = input("Un animal : ")
phrase = input("Une phrase : ")
verbe = input("Un verbe (à l'infinitif) : ")

histoire = f"Hier, je suis allé à {lieu} et j'ai rencontré un {animal} qui parlait {langue}. Il m'a dit : '{phrase}' puis il a {verbe}."
histoire2 = "Hier, je suis allé à " + lieu + " et j'ai rencontré un " + animal + " qui parlait " + langue + ". Il m'a dit : '" + phrase + "' puis il a " + verbe + "."

print("\nTon histoire :")
print(histoire+"\n"+histoire2)