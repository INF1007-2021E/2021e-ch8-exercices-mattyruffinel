#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import json
import csv
from recettes import add_recipes,print_recipe
import sys
import pickle

# TODO: Définissez vos fonction ici
def compare_fichier(path1=str,path2=str):
    with open(path1) as fichier1,open(path2) as fichier2:
        for thing in fichier1:
            if thing not in fichier2:
                print(f"les fichiers sont differents a {thing} ")
                break
            else:
                print('les fichiers sont identiques')

def triple_espace(path1=str,path2=str):
    with open(path1)as fichier1, open(path2,"w") as fichier2:
        fichier2.write(fichier1.read().replace(" ","   "))

def note_correspond(path1,path2):
    with open(path1,"r")as fichier1, open(path2,"w")as fichier2:
        ligne = fichier1.readline()
        for note in ligne:
            for valeur,chiffre in PERCENTAGE_TO_LETTER.items():
                if chiffre[0] <= int(note.rstrip()) < chiffre[1]:
                    fichier2.write(f'{note.rstrip()}   {valeur}')

def conservation(recipe_path1):
    if recipe_path1 and os.path.exist(recipe_path1):
        recipe=pickle.load(open(recipe_path1,"rb"))
    else:
    recipe= dict()

    while True:
        choice=input("choisisser une option: a) ajouter une recette: \n b)Modifier une recette: \n c)Supprimer une recette : d) Afficher une recette: \n e)Quitter le programme ")
        if choice=="a":
            recipe=add_recipes(recipe)
        elif choice=="b":
            pass
        elif choice=="c":
            pass
        elif choice=="d":
            print_recipe(ingredients)
        elif choice=="e":
            pass
        else:
            print("L'option choisi n'est pas valide")










if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare_fichier('exemple.txt','notes.txt')

    conservation("exemple2.txt")

    pass
