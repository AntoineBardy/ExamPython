import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = [ "examen" , "python" , "bouche" , "cheval" , "purger" , "souris", "france", "bateau" , "animal" , "bronze" ]
Mot = random.choice(listeMot)
print (Mot)

def chercheLettre (lettre, mot):
	for i in range (len(mots)):
		if lettre == mots[i]:
		return

def oneLettre (lettre, indiceLettre, mot):
	if lettre in mot:
		if mot[indiceLettre] == motChoisis[indiceLettre]:
			print(Fore.RED + lettre, end=" ")
			return
		print(Fore.YELLOW + lettre, end=" ")
		return
	print(Fore.BLUE + lettre, end=" ")


def nombreDeFois (lettre, mot):
	for i in range(len(mots)):
		chercheLettre (lettre)
		print ()
