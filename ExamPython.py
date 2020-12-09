import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = [ "examen" , "python" , "bouche" , "cheval" , "purger" , "souris", "france", "bateau" , "animal" , "bronze" ]
Mot = random.choice(listeMot)
print (Mot)

for Tentative in range (0,8):
	JoueurTry = input("Saisir un mot de 6 lettre uniquement : ")
	for i in range (0,6):
		if mot[i] == JoueurTry [i]
			print(Fore.RED + , JoueurTry)
		else : 
			couleur : False
			for j in range (0,6):
				if mot[i] == JoueurTry[j]
					print(Fore.YELLOW + , JoueurTry)