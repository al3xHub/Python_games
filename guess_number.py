import random
'''
print("Hello, what is your name?")
name=input()
print("Cool "+name+". I am thinking a number between 1 and 20, take a guess dude!")
number=random.randint(1,20)
guess_number=input()
guess_number= int(guess_number)
while guess_number>number or guess_number<number:
    if guess_number>number:
        print("Thats too high, try again")
        guess_number=input()
        guess_number= int(guess_number)
    elif guess_number<number:
         print("Thats too low, try again")
         guess_number=input()
         guess_number= int(guess_number)
print("You are the winner!! The number was: ",number)
'''
guesses_taken=0
number=random.randint(1,20)

print("Hello, what is your name?")
name=input()
print("Cool "+name+". I am thinking a number between 1 and 20, take a guess dude!")
guess_number=input()
guess_number=int(guess_number)

for guesses_taken in range(5):
    if guess_number>number:
        print("That's to high, try again...")
        guess_number=input()
        guess_number= int(guess_number)
    elif guess_number<number:
        print("That's to low, try again come on...")
        guess_number=input()
        guess_number= int(guess_number)
    else:
        break

if guess_number==number:
    print("You are the winner!!, you have been trying for ",guesses_taken+1, "times.The random number is: ",number)
elif guess_number!=number:
    print("you lose... The number i was thinking of is",number)






