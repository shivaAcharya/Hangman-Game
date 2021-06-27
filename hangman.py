#! python3
# hangman.py - A hangman game with 8 available guesses

import random, string

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
    result = True
    for char in secretWord:
      if char not in lettersGuessed:
        result = False
        break
    return result

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    for char in secretWord:
      if char in lettersGuessed:
        guessedWord += char
      else:
        guessedWord += '_ '
    return guessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remAlphabets = str(string.ascii_lowercase)
    for char in lettersGuessed:
      if char in remAlphabets:
        remAlphabets = remAlphabets.replace(char, '')
    return remAlphabets
    
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

    '''
    remTries = 8    # No. of guesses remaining
    lettersGuessed = []

    # Print game introduction
    print("  ", 'Welcome to the game, Hangman!')
    print("  ", "I am thinking of a word that is", len(secretWord), "letter(s) long.")
    
    # Loop until guess is correct or tries run out
    while remTries > 0 and not isWordGuessed(secretWord, lettersGuessed):
      print("  ", "------------")
      print("  ", "You have", remTries, "guess(es) left." )
      print("  ", "Available letters:", getAvailableLetters(lettersGuessed))

      guess = input("   Please guess a letter: ") # Get users input

      if guess in lettersGuessed: 
        print("  ", "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
      else:
        lettersGuessed.append(guess)
        if guess in secretWord:
          print("  ", "Good guess: ", getGuessedWord(secretWord, lettersGuessed))  
        else:
          print("  ", "Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
          remTries -= 1
    
    print("  ", "------------")

    if remTries == 0:
      print("  ", "Sorry, you ran out of guesses. The word was", secretWord)
    
    if isWordGuessed(secretWord, lettersGuessed):
      print("  ", "Congratulations, you won!")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
