# Codecademy Backend Challenge
# CREATED BY: Diana Arreola
# DESCRIPTION: Model that gives predictions on whether an advertisement has the
import random
import os
import math
import ufo as ufo

# handle capitalized letters
# handle giant print statements
# handle non single letter guesses/input
# handle if the person wins
# handle if the person loses
# handle asking the person if they want to play again

def randomizeNoun():
    """ randomeizeNoun returns a random noun (str) from 
        the nouns.txt file 
    """
    with open("nouns.txt") as noun_file:
        nouns = noun_file.read().split()
    random_noun = random.choice(nouns)
    return random_noun


def addGuessedLetter(word,letter,dashed_codeword):
    """ findIndexOfLetter returns the index at which 
        the parameter letter is in word
        input: the codeword (str), the letter guessed (str)
               and the guessed codeword (str)
        output: correctly guessed
    """
    # multiple occurences of a letter
    dashed_codeword = list(dashed_codeword)
    for i in range(len(word)):
        if word[i] == letter:
            dashed_codeword[i] = letter
    print(''.join(dashed_codeword))
    return ''.join(dashed_codeword)


#  keep state of codeword in dashes, store in array 
def UFOGame():
    """ UFO GAME
    """
    codeword = randomizeNoun()
    len_codeword = len(codeword)
    guessed_codeword = len_codeword*'_'
    incorrect_guesses = []
    chances_left = 6

    #  initial showcase
    print("UFO: The Game")
    print("Instructions: save us from alien abduction by guessing letters in the codeword.")
    print(ufo.x[0])
    print("Incorrect guesses: ")
    print("None")
    print("Codeword: ")
    print(guessed_codeword)
    letter_guessed = input("Please enter your guess: ")
    letter_guessed = letter_guessed.lower()

    while chances_left != 0:

        if letter_guessed in codeword:
            # replace dash with right letter
            guessed_codeword = addGuessedLetter(codeword, letter_guessed, guessed_codeword)

            # display correct
            print("Correct! You're closer to cracking the codeword.")
            print(ufo.x[abs(chances_left-6)])
            print("Already Guessed That!")
            print("Incorrect guesses: ")
            print(' '.join(letter for letter in incorrect_guesses))
            print("Codeword: ")
            print(guessed_codeword)
            letter_guessed = input("Please enter your guess: ")
            letter_guessed = letter_guessed.lower()

            

           
        elif letter_guessed in incorrect_guesses:
            chances_left -= 1

            # display correct
            print("Incorrect! The tractor beam pulls the person in further.")
            print(ufo.x[abs(chances_left-6)])
            print("Already Guessed That!")
            print("Incorrect guesses: ")
            print(' '.join(letter for letter in incorrect_guesses))
            print("Codeword: ")
            print(guessed_codeword)
            letter_guessed = input("Please enter your guess: ")
            letter_guessed = letter_guessed.lower()

        elif letter_guessed not in codeword:
            # add capletter in incorrect guesses array
            incorrect_guesses.append(letter_guessed)
            chances_left -= 1

            # display correct
            print("Incorrect! The tractor beam pulls the person in further.")
            print(ufo.x[abs(chances_left-6)])
            print("Incorrect guesses: ")
            print(' '.join(letter for letter in incorrect_guesses))
            print("Codeword: ")
            print(guessed_codeword)
            letter_guessed = input("Please enter your guess: ")
            letter_guessed = letter_guessed.lower()

UFOGame()


