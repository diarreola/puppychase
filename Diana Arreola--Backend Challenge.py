# Codecademy Backend Challenge
# CREATED BY: Diana Arreola
# DESCRIPTION: Model that gives predictions on whether an advertisement has the
import random
import os
import math
import ufo as ufo

# handle capitalized letters
# handle giant print statements

# remove all print statements
# clean code
#  test code
# check for rules of requiremnt
# do bonus

def randomizeNoun():
    """ randomeizeNoun returns a random noun (str) from 
        the nouns.txt file 
    """
    with open("nouns.txt") as noun_file:
        nouns = noun_file.read().split()
    random_noun = random.choice(nouns)
    print(random_noun)
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

def validAnswer(dashed_codeword):
    dashed_codeword = list(dashed_codeword)
    for i in range(len(dashed_codeword)):
        if dashed_codeword[i] == '_':
            return False
    return True

def playAgain(user_input):
    if (user_input == "N") | (user_input == "n") | (user_input == "No") | (user_input == "NO")| (user_input == "no"):
        print('Goodbye')
        return 1
    elif (user_input == "Y") | (user_input == "y") | (user_input == "Yes") | (user_input == "yes") | (user_input == "YES"):
        print('Lets play again')
        return UFOGame()
    else:
        print('I did not understand you. Bye!')
        return 1

def checkInput(user_input):

    len_input = len(user_input)
    if len_input > 1:
        print('Please only guess one letter')
        return ' '
    else:
        return user_input

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
    checkInput(letter_guessed)
    letter_guessed = letter_guessed.lower()

    while chances_left != 0:

        if letter_guessed in codeword:
            # replace dash with right letter
            guessed_codeword = addGuessedLetter(codeword, letter_guessed, guessed_codeword)
            
            # check if the answer is correct
            if validAnswer(guessed_codeword):
                print("Correct! You saved the person and earned a medal of honor!")
                print("The codeword is: ", codeword, ".")
                answer = input("Would you like to play again (Y/N)?")
                playAgain(answer)
            else:
                print("Correct! You're closer to cracking the codeword.")
                print(ufo.x[abs(chances_left-6)])
                print("Already Guessed That!")
                print("Incorrect guesses: ")
                print(' '.join(letter for letter in incorrect_guesses))
                print("Codeword: ")
                print(guessed_codeword)
                letter_guessed = input("Please enter your guess: ")
                letter_guessed = checkInput(letter_guessed)
                

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
            letter_guessed = checkInput(letter_guessed)

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
            letter_guessed = checkInput(letter_guessed)
    # Lost the Game
    print("Incorrect! The tractor beam pulls you all the way in. You Lost.")
    print("The codeword is: ", codeword, ".")
    answer = input("Would you like to play again (Y/N)?")
    playAgain(answer)
    

UFOGame()




