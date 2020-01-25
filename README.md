# codecademychallenge

How to play:

Guess one letter at a time of a codeword represented by blank placeholders for each letter. If the letter does not exist in the codeword, the person is pulled in closer to the UFO by the tractor beam. If the letter exists, the blanks that correspond to the position of those letters in the codeword are replaced by the letter. If all the letters of the codeword are revealed before the person is pulled into the UFO, you win. Otherwise, the UFO abducts the person and you lose.

Rules and requirements:

All valid codewords are chosen from this dictionary of English words
The codeword is represented by a series of dashes, one per letter in the codeword []
The codeword is chosen randomly at the start of the game []
Each game starts with the person at the bottom of the beam. Upon guessing a letter that does not exist in the codeword, the person is lifted one row. []
The distance of the person’s feet to the UFO is six rows, so unless you solve the codeword, you lose on the sixth incorrect guess. []
Every letter that was guessed but does not exist in the codeword is displayed and cannot be guessed again []
Every letter that was guessed that exists in the codeword replaces the dashes for all instances in which they exist in that word []
You win when all the dashes in the codeword have been replaced by your correct guesses []
The game should read user input on the command line and allow the user to start a new game after completing one. []
The game should identify whether a guess was correct or not []
The game should display the current state of abduction by the UFO. Snippets of code that represent each state of UFO abduction have been provided in a few popular languages for your convenience. []

How you will be evaluated

Requirements are all met. The game plays as described in the Rules and requirements section above. []
Code is well-organized and easy to read/understand. []
Any algorithms or data structures used are appropriate and reasonably efficient. []
Unit tests are written to determine that code is correct. []
Bonus 

Display how many words in the provided dictionary are potentially correct codewords given the correct and incorrect letter guesses made so far. For example, suppose the game was in this state: []
