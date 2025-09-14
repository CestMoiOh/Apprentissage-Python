# Demande à l'utilisateur les différents paramètres
res = 0
a,b = map(float, input("Donne moi deux nombres").split())
opérateur = input("Donne moi un opérateur(+,-,*,/)")

# Traitement de l'opérateur
if opérateur == "+":
    res = a+b
elif opérateur == "-":
    res = a-b
elif opérateur == "*":
    res = a*b
elif opérateur == "/":
    if b==0:
        ""
    else:
        res = a/b
else:
    print("opérateur non valide, veuillez entrer un opérateur valide")

# Affichage du résultat
if opérateur=="/" and b==0:
    print("Division par 0 impossible")
else:
    print(a, opérateur, b, "=", res)