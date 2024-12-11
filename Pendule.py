
import random
mots = "language programmation vlan routeur switch  address machine learning"

mots = mots.split()

index_secret = random.randint(0, len(mots) - 1 )

donnees = {
    "mot_secret" : mots[index_secret],
    "mot_deviner" : "_" * len(mots[index_secret]),
    "points" : 10,
    "historique": set()
        }

print(f'-:-:{donnees["mot_deviner"]} le mot à deviner a ({len(donnees["mot_deviner"])} lettres) -:-:- vous avez un score de: {donnees["points"]} points')
while True:
   
    lettre = input("--renseignez une lettre: ")
    donnees["historique"].add(lettre)
    if lettre in donnees["mot_secret"] and lettre not in donnees["mot_deviner"]:
        liste = list(donnees["mot_deviner"])
       
        for i, lettre_secret in enumerate(donnees["mot_secret"]):
            if lettre == lettre_secret:
                liste[i] = lettre
        donnees["mot_deviner"] = ''.join(liste)
    elif lettre not in  donnees["mot_secret"]:
        donnees["points"] -=1
    count = 0
    for i in   donnees["mot_deviner"]:
        if i == '_':
            count += 1  
    print(f'''-:-:{donnees["mot_deviner"]} -:-:- score : {donnees["points"]} point(s). {count} lettre(s) restantes:. lettre(s) renseignées {donnees["historique"]}''')
    
    if '_' not in donnees["mot_deviner"]:
        print(f"-:-:- Félicitaions, vous avez gagné la partie avec un score de {donnees["points"]} point(s) !!! -:-:-")
        break
    
    if donnees["points"] == 0:
        print('__Malheuresement vous avez perdu la partie.__La prochaine fois ça sera la bonne, mola!')
        break