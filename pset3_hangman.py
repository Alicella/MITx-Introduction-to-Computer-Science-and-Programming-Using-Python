# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    flag = True
    for w in secretWord:
        if w not in lettersGuessed:
            flag = False
            break
    return flag


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedword = ''
    for w in secretWord:
        if w in lettersGuessed:
            guessedword += w
        else:
            guessedword += '_ '
    return guessedword


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = list(string.ascii_lowercase)
    for l in letters[:]:
        if l in lettersGuessed:
            letters.remove(l)

    return ''.join(map(str, letters))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess about whether their guess appears in the computers word.
    * After each round, you should also display to the user the partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")

    lt = len(secretWord)
    print("I'm thinking of a word that is " + str(lt) + " letters long.\n")

    guess = 8
    lettersGuessed = []
    # aval = string.ascii_lowercase

    while guess > 0:
        print("You have " + str(guess) + " guesses left.")
        aval = getAvailableLetters(lettersGuessed)
        print("Available letters: " + aval)

        newletter = input("Please guess a letter: ")
        lettersGuessed.append(newletter)
        gsdw = getGuessedWord(secretWord, lettersGuessed)

        if newletter in secretWord and newletter in aval:
            print("Good guess: " + gsdw)

        elif newletter not in aval:
            guess -= 1
            print("Oops! You've already guessed that letter :" + gsdw)

        else:
            guess -= 1
            print("Oops! That letter is not in my word: " + gsdw)

        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break

    if not isWordGuessed(secretWord, lettersGuessed):
        print("Sorry, you ran out of guesses. The word was else. ")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
