#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import json
import csv


# TODO: Définissez vos fonction ici
def compare_fichier(path1=str,path2=str):
    fichier1=open(path2)
    fichier2=open(path1)
    for thing in fichier1:
        if thing not in fichier2:
            print(f"les fichiers sont differents a {thing} ")
            break
        else:
            print('les fichiers sont identiques')


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare_fichier('exemple.txt','notes.txt')
    pass
