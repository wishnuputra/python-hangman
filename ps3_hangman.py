# ========================================================================
# HANGMAN GAME
# ========================================================================
# 
# This is a program for running a hangman game. This game is written
# in Python.
#
# The program will generate secret word randomly. Then the player
# will guess the letter until they can correctly guess the word or
# he/she has guessed wrongly for 8 times.
#
# Created on Wed Jun 26 19:55:21 2019
#
# @author: Wishnuputra
# ========================================================================

import random
import string

WORDLIST_FILENAME = "words.txt"

# helper code
# -----------------------------------
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
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
        


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += ' _ '
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        availableLetters.remove(letter)

    return ''.join(availableLetters)
    


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    guessLeft = 8
    guessedWord = ""
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    print("-----------")
    
    while True:
        availableLetter = getAvailableLetters(lettersGuessed)
        print("You have", guessLeft, "guesses left.")
        print("Available letters:", availableLetter)
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        
        if guess not in availableLetter:
            print("Oops! You've already guessed that letter:", guessedWord)
        else:
            lettersGuessed.append(guess)
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            if guess in guessedWord:
                print("Good guess:", guessedWord)
            else:
                print("Oops! That letter is not in my word:", guessedWord)
                guessLeft -= 1
                
        print("-----------")
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        if guessLeft == 0:
            print("Sorry, you rant out of guesses. The word was", secretWord)
            break
        
    
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
