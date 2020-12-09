import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = [ "examen" , "python" , "bouche" , "cheval" , "purger" , "souris", "france", "bateau" , "animal" , "bronze" ]
Mot = random.choice(listeMot)
print (Mot)
