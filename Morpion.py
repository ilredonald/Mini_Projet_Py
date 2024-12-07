grille = [
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . '],
    [' . ', ' . ', ' . ']
]
    
def terrain():
    ''''
    cette fonction affiche la table de jeu.'''
    for i in range(len(grille)):
        for j in range(len(grille)):
            print(grille[i][j], end='')
        print()
def victoire()-> bool:
    '''
    cette fonction vérifie si les symboles sont identiques soit sur une ligne,
    soit sur une colonne, soit sur la diagonale et retourne False sinon.'''
    for i in range(len(grille)):
        if grille[i][0] == grille[i][1] == grille[i][2] != ' . ':
            return True 
    for i in range(len(grille)):
        if grille[0][i] == grille[1][i] == grille[2][i] != ' . ':
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] != ' . ':
            return True 
    elif grille[2][0] == grille[1][1] == grille[0][2] != ' . ':
            return True 
    return False
def egalite()-> bool:
    """
    cette fonction vérifie si toutes les cases sont occupées et retourne False sinon.
    """
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] != ' . ':
                return False
    return True
joueur = "Joueur 1"     
#grille()
while True:
    choix = int(input(f'--: {joueur} :-- choisir un numéro [1-9]: '))
    if choix in range(1, 10) :
        colonne = (choix - 1) % 3
        ligne = (choix - 1) // 3
        if  grille[ligne][colonne] == ' . ':
            grille[ligne][colonne] = ' x ' if joueur == 'Joueur 1' else ' o '
            terrain()
            if victoire():
                print(f"--: {joueur} :--Félicitations! vous avez gagné la partie!")
                joueur = "Joueur 1" if joueur == "Joueur 2" else "Joueur 2"
                print(f"--: {joueur} :--Désolé! Pas de chance!")
                break   
            elif egalite():
                print('vous avez fait un match nul!')
                break
            joueur = "Joueur 1" if joueur == "Joueur 2" else "Joueur 2"
        else:
            print("cette case est déjà prise, choississez en une autre!")
    else:
        print(f"--: {joueur} :--vous devez choisir un chiffre entre 1 et 9! Réessayez: ")
    