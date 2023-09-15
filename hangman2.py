import random

HANGMAN_PICS=['''
    +---+
        |
        |
        |
       ===
''','''
    +---+
    O   |
        |
        |
       ===
''','''
    +---+
    O   |
    |   |
        |
       ===
''','''
    +---+
    O   |
    |   |
   /    |
       ===
''','''
    +---+
    O   |
    |   |
   / \  |
       ===
''','''
    +---+
    O   |
   /|   |
   / \  |
       ===
''','''
    +---+
    O   |
   /|\  |
   / \  |
       ===
''']

words="cat miau sol michi".split()

def get_secret_word(word_list):
    word_index=random.randint(0,len(word_list)-1)
    return word_list[word_index]

def display_board(missed_letters,correct_letters,secret_word):
    print(HANGMAN_PICS[len(missed_letters)]) 
    blanks="_"*len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks=blanks[:i]+secret_word[i]+blanks[i+1:]
        
    for letter in blanks:
        print(letter,end=" ")

def get_guess(already_guessed):
    while True:
        print("Guess a letter")
        guess=input()
        guess=guess.lower()

        if len(guess) !=1:
            print("Introduce a single letter")
        elif guess in already_guessed:
            print("You already guess this letter, try another one.")
        elif guess not in "abcdefghijklmnñopqrstuvwxyz":
            print("Please introduce a LETTER")
        else:
            return guess
        
def play_again():
    print("Do you wanna play again?(yes or no)")
    return input().lower().startswith("y")

print("H A N G M A N")
missed_letters=""
correct_letters=""
secret_word=get_secret_word(words)
game_done=False

while True:
    display_board(missed_letters,correct_letters,secret_word)
    guess=get_guess(missed_letters+correct_letters)

    if guess in secret_word:
        correct_letters=correct_letters+guess

        found_letters=True

        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_letters=False
                break
    
        if found_letters:
            print("Yes! The secret word is "+secret_word.upper()+". YOU ARE THE WINNER!!")
            print('''
                     /\_/\ 
                    ( o.o )
                     > ^ <
                  ''')
            game_done=True

    else:
        missed_letters=missed_letters+guess

        if len(missed_letters)==len(HANGMAN_PICS)-1:
            display_board(missed_letters,correct_letters,secret_word)
            print("You have run out of guesses!\nAfter "+str(len(missed_letters))+"missed guesses and "+str(len(correct_letters))+" correct guesses, the word was "+secret_word.upper())
            print('''
                      _____ ____  _      _____   ____  _     _____ ____ 
                    /  __//  _ \/ \__/|/  __/  /  _ \/ \ |\/  __//  __\ 
                    | |  _| / \|| |\/|||  \    | / \|| | //|  \  |  \/|
                    | |_//| |-||| |  |||  /_   | \_/|| \// |  /_ |    /
                     \____\\_/ \|\_/  \|\____\  \____/\__/  \____\\_/\_\ 
                ''')
            game_done=True
    if game_done:
        if play_again():
            missed_letters=""
            correct_letters=""
            game_done=False
            secret_word=get_secret_word(words)
        else:
            break