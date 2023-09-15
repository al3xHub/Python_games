import random
import time
from anyio import sleep

num_random=random.randint(1,2)
start=True

while start==True:
    print("You are in a land full of dragons...")
    time.sleep(3)
    print("In front of you, you see two caves.\nIn one cave, the dragon is friendly and will share his treasure with you.")
    time.sleep(6)
    print("The other dragon is greedy and hungry, and will eat you on sight.")
    time.sleep(6)
    print("Which cave will you go into? (1 or 2)")
    selection=input()
    selection=int(selection)

    if selection==1 or 2:

        if selection==num_random:
            print("You approach the cave...")
            time.sleep(3)
            print("It is dark and spooky...")
            time.sleep(5)
            print("A large dragon jumps out in front of you! He opens his jaws and...")
            time.sleep(3)
            print("Gobbles you down in one bite!")
            time.sleep(2)
            print("hahaha you lose, do you want to play again?(yes or no)")
            response=input()
            if response=="no":
                start=False

        elif selection!=num_random:
            print("You approach the cave...")
            time.sleep(3)
            print("It is dark and spooky...")
            time.sleep(5)
            print("A large dragon jumps out in front of you! He opens his jaws and...")
            time.sleep(3)
            print("Gives you a his treasure!")
            time.sleep(2)
            print("YOU WIN!!, do you want to play again?(yes or no)")
            response=input()
            if response=="no":
                start=False

    elif selection != 1 or 2:
        print("Lo siento, debes escribir las opciones (1 o 2)")
