import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = [ "examen" , "python" , "bouche" , "cheval" , "purger" , "souris", "france", "bateau" , "animal" , "bronze" ]
Mot = random.choice(listeMot)
print (Mot)

for Tentative in range (0,8):
	JoueurTry = input("Saisir un mot de 6 lettre uniquement : ") 