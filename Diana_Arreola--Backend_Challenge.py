# Codecademy Backend Challenge
# CREATED BY: Diana Arreolals
import random
import os
import math
import sys
import ufo as ufo

def randomizeNoun():
    """ randomeizeNoun returns a random noun (str) from 
        the nouns.txt file 
    """
    with open("nouns.txt") as noun_file:
        nouns = noun_file.read().split()
    random_noun = random.choice(nouns)
    random_noun = random_noun.upper()
    return random_noun

def addGuessedLetter(codeword,letter,dashed_codeword):
    """ addGuessedLetter returns the guessed codeword with the
        correct guessed letter added to it
        input: the codeword (str), the letter guessed (str)
               and the guessed codeword (str)
        output: guessed codeword (str)
    """
    dashed_codeword = list(dashed_codeword)
    for i in range(len(codeword)):
        if codeword[i] == letter:
            dashed_codeword[i] = letter
    print(''.join(dashed_codeword))
    return ''.join(dashed_codeword)

def validAnswer(dashed_codeword):
    """ validAnswer returns T if the guessed codeword is 
        guessed correctly and False if the guessed codeword
        is not guessed completely
        input: the guessed codeword (str)
        output: True or False (Boolean)
    """
    dashed_codeword = list(dashed_codeword)
    for i in range(len(dashed_codeword)):
        if dashed_codeword[i] == '_':
            return False
    return True

def userInput():
    """ userInput returns the users input
        output: user input (str)
    """
    letter_guessed = input("Please enter your guess: \n")
    letter_guessed = checkInput(letter_guessed)
    letter_guessed = letter_guessed.upper()
    return letter_guessed

def playAgain(user_input):
    """ playAgain either ends the game or restarts the game 
        based on the user input.
        input: user input (str)
        output: game ends or game restarts
    """
    if (user_input == "N") | (user_input == "n") | (user_input == "No") | (user_input == "NO")| (user_input == "no"):
        print('Goodbye')
        sys.exit()
    elif (user_input == "Y") | (user_input == "y") | (user_input == "Yes") | (user_input == "yes") | (user_input == "YES"):
        print('Lets play again')
        return UFOGame()
    else:
        print('I did not understand you. Bye!')
        return 0

def checkInput(user_input):
    """ checkInput checks whether a users input is a valid
        letter. If it is not, ' ' is returned. If it is, 
        the users input is returned
        input: user input (str)
        output: ' '(str) or user
    """
    intArr = ['1','2','3','4','5','6','7','8','9','0']
    specialChars = ['+', '-', '&', '|', '!', '(', ')', '{', '}', '[', ']', '^',
                '~', '*', '?', ':', '/','<','>','.',',',';','$','%','*']

    len_input = len(user_input)
    if len_input > 1:
        print('Please only guess one letter.\n')
        return ' '
    elif user_input in intArr:
        print('Please only guess letters not numbers.\n')
        return ' '
    elif user_input in specialChars:
        print('Please only guess letters not special characters.\n')
        return ' '
    else:
        return user_input

def correctGuess(chances_left, incorrect_guesses, guessed_codeword):
    """ correctGuess handles the case where the user 
        guesses a letter correctly.
        input: chances left to play (str), the codeword (str)
               , the array of incorrect guesses of letters (arr),
               and the guessed codeword (str)
        output: chances left to play (str) and new letter guessed 
                from user (str)
    """
    print("Correct! You're closer to cracking the codeword.\n")
    print(ufo.x[abs(chances_left-6)])
    print("Incorrect guesses: ")
    print(' '.join(letter for letter in incorrect_guesses))
    print("Codeword: ")
    print(guessed_codeword)
    print("Number of dictionary matches:")
    print(bonusWords(incorrect_guesses,guessed_codeword))
    letter_guessed = userInput()
    return letter_guessed

def incorrectGuess(chances_left, codeword, incorrect_guesses, guessed_codeword):
    """ incorrectGuess handles the case where the user 
        guesses a letter incorrectly.
        input: chances left to play (str), the codeword (str)
               , the array of incorrect guesses of letters (arr),
               and the guessed codeword (str)
        output: chances left to play (str) and new letter guessed 
                from user (str)
    """
    chances_left -= 1

    # lost game
    if chances_left == 0:
        return lostGame(codeword)

    # incorrect guess
    print("Incorrect! The tractor beam pulls the person in further.\n")
    print(ufo.x[abs(chances_left-6)])
    print("Incorrect guesses: ")
    print(' '.join(letter for letter in incorrect_guesses))
    print("Codeword: ")
    print(guessed_codeword)
    print("Number of dictionary matches:")
    print(bonusWords(incorrect_guesses,guessed_codeword))
    letter_guessed = userInput()
    return chances_left, letter_guessed

def lostGame(codeword):
    """ lostGame prints ou losing statement and asks for 
        user prefernce
        input: the codeword (str)
        output: game ends or game restarts based on user 
        prefernce
    """
    print("Incorrect! The tractor beam pulls you all the way in. You Lost.\n")
    print("The codeword is: ", codeword, ".")
    answer = input("Would you like to play again (Y/N)?\n")
    return playAgain(answer)

def wonGame(codeword):
    """ wonGame prints ou winning statement and asks for 
        user prefernce
        input: the codeword (str)
        output: game ends or game restarts based on user 
        prefernce
    """
    print("Correct! You saved the person and earned a medal of honor!\n")
    print("The codeword is: ", codeword, ".")
    answer = input("Would you like to play again (Y/N)?\n")
    
    return playAgain(answer)

def bonusWords(incorrect_guesses, guessed_codeword):
    """ bonusWords displays how many words 
        in the provided dictionary are potentially 
        correct codewords given the correct and 
        incorrect letter guesses made so far.
        input: the codeword (str), the array of 
                incorrect letters guessed (arr) 
        output: an integer which is the amount of matches
                in the dict
    """
    len_codeword = len(guessed_codeword)
    # array of wprd
    with open("nouns.txt") as noun_file:
        nouns = noun_file.read().split()
    # first filter by codeword length
    appropriate_length = list(filter(lambda x: len(x)==len_codeword,nouns))
  
    # initialize dictionary
    appropriate_letters = {}
    for word in appropriate_length:
        appropriate_letters[word] = 0

    # filter out incorrect letters using the incorrect guesses array
    # from the appropriate length array
    # Utilizing a dictionary to associate every word in appropriate length
    # with a key value that represents the number of incorrect letters in it 
    filtered_words = []
    for i in incorrect_guesses:
        for j in appropriate_length:
            if i in j:
                appropriate_letters[i] += 1
    for i in appropriate_letters:
        if appropriate_letters[i] == 0:
            filtered_words.append(i)

    # Find the char and index of the letters in
    # the guessed codeword
    letterAndIndex = findLetterAndIndex(guessed_codeword)
    
    # Find the possible bonus words
    bonusWords = compareStrings(filtered_words, letterAndIndex)

    return len(bonusWords)

def findLetterAndIndex(guessed_codeword):
    """ bonusWords displays how many words 
        in the provided dictionary are potentially 
        correct codewords given the correct and 
        incorrect letter guesses made so far.
        input: the guessed codeword (str) 
        output: dict of correct guessed letters
                associated with its index
    """
    # gives letter and index of word
    letter = {}
    for i in range(len(guessed_codeword)):
        if guessed_codeword[i] != '_':
            letter[guessed_codeword[i]] = i
    return letter

def compareStrings(filtered_words, letterAndIndex):
    """ compareStrings is a helper function for bonus
        words that compares the current guessed codeword
        againt the pre-filtered words
        input: an array of pre-filtered words (arr)
              and dict of correct letter and index
        output: an array of the possible dictionary matched
    """
    bonusWords = {} 
    # initialize dictionary
    for word in filtered_words:
        bonusWords[word] = 0

    for char in letterAndIndex:
        for i in range(len(filtered_words)):
            if filtered_words[i][letterAndIndex[char]].upper() == char:
                bonusWords[filtered_words[i]] += 1 
    letter_length = len(letterAndIndex)
    bonus = []
    for word in bonusWords:
        if bonusWords[word] == letter_length:
            bonus.append(word)
    return bonus
 
def UFOGame():
    """ UFO GAME returns a game for guessing a codeword 
        one letter at a time. If the letter does not 
        exist in the codeword, the person is pulled in 
        closer to the UFO by the tractor beam. If the letter 
        exists, the blanks that correspond to the position 
        of those letters in the codeword are replaced by 
        the letter. If all the letters of the codeword 
        are revealed before the person is pulled into the 
        UFO, you win. Otherwise, the UFO abducts the person 
        and you lose.
    """
    codeword = randomizeNoun()
    len_codeword = len(codeword)
    guessed_codeword = len_codeword*'_'
    incorrect_guesses = []
    chances_left = 6

    #  initial display
    print("UFO: The Game\n")
    print("Instructions: save us from alien abduction by guessing letters in the codeword.\n")
    print(ufo.x[0])
    print("Incorrect guesses: ")
    print("None\n")
    print("Codeword: ")
    print(guessed_codeword,"\n")
    letter_guessed = userInput()

    while chances_left != 0:

        if letter_guessed in guessed_codeword:
            print("You can only guess that letter once, please try again.\n")
            letter_guessed = userInput()
       
        elif letter_guessed in codeword:

            guessed_codeword = addGuessedLetter(codeword, letter_guessed, guessed_codeword)
            
            # checks codeword is correct
            if validAnswer(guessed_codeword):
                return wonGame(codeword)
               
            else:
                letter_guessed = correctGuess(chances_left, incorrect_guesses, guessed_codeword)
                 
        elif letter_guessed in incorrect_guesses:
            print("Already Guessed That!\n")
            letter_guessed = userInput()

        elif letter_guessed not in codeword:
            if letter_guessed != ' ' and letter_guessed != '':

                incorrect_guesses.append(letter_guessed)
                chances_left,letter_guessed = incorrectGuess(chances_left, codeword, incorrect_guesses, guessed_codeword) 
            else:
                print("I cannot understand your input.\n")
                letter_guessed = userInput()
                
def main():
  UFOGame()
  
if __name__== "__main__":
  main()     






