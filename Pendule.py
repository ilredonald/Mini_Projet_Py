
import random
mots = "stupide authentique festival content laver le cerveau gymnastique"

mots = mots.split()

index_secret = random.randint(0, len(mots) - 1 )

donnees = {
    "mot_secret" : mots[index_secret],
    "mot_deviner" : "_" * len(mots[index_secret]),
    "points" : 10
}

while True:
    lettre = input("--renseignez une lettre: ")
    
    if lettre in donnees["mot_secret"] and lettre not in donnees["mot_deviner"]:
        liste = list(donnees["mot_deviner"])
        for i, lettre_secret in enumerate(donnees["mot_secret"]):
            if lettre == lettre_secret:
                liste[i] = lettre
        donnees["mot_deviner"] = ''.join(liste)
    elif lettre not in  donnees["mot_secret"]:
        donnees["points"] -=1
        
    print(f'-:-:{donnees["mot_deviner"]} -:-:- score: {donnees["points"]}')
    
    if '_' not in donnees["mot_deviner"]:
        print(f"-:-:- Félicitaions, vous avez gagné la partie avec un score de {donnees["points"]} !!! -:-:-")
        break
    
    if donnees["points"] == 0:
        print('__Malheuresement vous avez perdu la partie.__La prochaine fois ça sera la bonne mola!')
        break