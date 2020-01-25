# Codecademy Backend Challenge
# CREATED BY: Diana Arreola
# DESCRIPTION: Model that gives predictions on whether an advertisement has the
import random
import os
import math
import ufo as ufo

# check number and characters
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
    random_noun = random_noun.upper()
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
        return 0
    elif (user_input == "Y") | (user_input == "y") | (user_input == "Yes") | (user_input == "yes") | (user_input == "YES"):
        print('Lets play again')
        return UFOGame()
    else:
        print('I did not understand you. Bye!')
        return 0

def checkInput(user_input):

    len_input = len(user_input)
    if len_input > 1:
        print('Please only guess one letter')
        return ' '
    else:
        return user_input

def incorrectGuess(chances_left, codeword, incorrect_guesses, guessed_codeword):
    chances_left -= 1

    # lost game
    if chances_left == 0:
        return lostGame(codeword)

    # incorrect guess
    print("Incorrect! The tractor beam pulls the person in further.")
    print(ufo.x[abs(chances_left-6)])
    print("Incorrect guesses: ")
    print(' '.join(letter for letter in incorrect_guesses))
    print("Codeword: ")
    print(guessed_codeword)
    letter_guessed = input("Please enter your guess: ")
    letter_guessed = checkInput(letter_guessed)
    letter_guessed = letter_guessed.upper()
    return chances_left, letter_guessed

def lostGame(word):
    print("Incorrect! The tractor beam pulls you all the way in. You Lost.")
    print("The codeword is: ", word, ".")
    answer = input("Would you like to play again (Y/N)?")
    return playAgain(answer)

def wonGame(word):
    print("Correct! You saved the person and earned a medal of honor!")
    print("The codeword is: ", word, ".")
    answer = input("Would you like to play again (Y/N)?")
    
    return playAgain(answer)

#  keep state of codeword in dashes, store in array 
def UFOGame():
    """ UFO GAME
    """
    codeword = randomizeNoun()
    len_codeword = len(codeword)
    guessed_codeword = len_codeword*'_'
    incorrect_guesses = []
    chances_left = 6

    #  initial 
    print("UFO: The Game")
    print("Instructions: save us from alien abduction by guessing letters in the codeword.")
    print(ufo.x[0])
    print("Incorrect guesses: ")
    print("None")
    print("Codeword: ")
    print(guessed_codeword)
    letter_guessed = input("Please enter your guess: ")
    checkInput(letter_guessed)
    letter_guessed = letter_guessed.upper()

    while chances_left != 0:
        if letter_guessed in codeword:
            guessed_codeword = addGuessedLetter(codeword, letter_guessed, guessed_codeword)
            
            # checks codeword is correct
            if validAnswer(guessed_codeword):
                return wonGame(codeword)
               
            else:
                print("Correct! You're closer to cracking the codeword.")
                print(ufo.x[abs(chances_left-6)])
                print("Incorrect guesses: ")
                print(' '.join(letter for letter in incorrect_guesses))
                print("Codeword: ")
                print(guessed_codeword)
                letter_guessed = input("Please enter your guess: ")
                letter_guessed = checkInput(letter_guessed)
                letter_guessed = letter_guessed.upper()
                
        elif letter_guessed in incorrect_guesses:
            print("Already Guessed That!")
            chances_left,letter_guessed = incorrectGuess(chances_left, codeword, incorrect_guesses, guessed_codeword)

        elif letter_guessed not in codeword:
            incorrect_guesses.append(letter_guessed)
            chances_left,letter_guessed = incorrectGuess(chances_left, codeword, incorrect_guesses, guessed_codeword)
            
            
    
UFOGame()




