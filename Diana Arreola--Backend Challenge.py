# Codecademy Backend Challenge
# CREATED BY: Diana Arreola
# DESCRIPTION: Model that gives predictions on whether an advertisement has the
import random
import os
import ufo as ufo


# create tests for random noun
def randomizeNoun():
    """ randomeizeNoun returns a random noun from the
        nouns.txt file 
    """
    with open("nouns.txt") as noun_file:
        nouns = noun_file.read().split()
    random_noun = random.choice(nouns)
    return random_noun

def UFOGame():
    """ randomeizeNoun returns a random noun from the
        nouns.txt file 
    """
    codeword = randomizeNoun()

    #  initial showcase
    print("UFO: The Game")
    print("Instructions: save us from alien abduction by guessing letters in the codeword.")
    print(ufo.x[0])

UFOGame()


