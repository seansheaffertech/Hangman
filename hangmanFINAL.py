# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)


print('-------H-A-N-G-M-A-N--------')  

import random

WORDLIST_FILENAME = "C:/Users/ssheaffer/Desktop/python/6.00.1/hangman/words.txt"

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
    print(len(wordlist), "words loaded.")
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
    ans = True

    for k in secretWord:
        if k not in lettersGuessed:
            ans = False
    return ans 

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretNew = ''
    
    for i in secretWord:
        if i not in lettersGuessed:
            secretNew += '_ '
        else:
            secretNew += i + ' '

    return secretNew

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letters = string.ascii_lowercase
    useableLetters = ''
    
    for i in letters:
        if i not in lettersGuessed:
            useableLetters += i
    return useableLetters
    

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

            ####-O-U-T-S-I-D-E--V-A-R-I-A-B-L-E-S-####
    tries = 8
    win = False
    lettersGuessed = []
    available_letters = ''
    gameOverLose = 'Sorry you ran out of guesses. The word was ' + secretWord + '.'
    gameOverWin = 'Congratulations, you won!'
    result = ''

            ####-I-N-T-R-O--D-I-S-P-L-A-Y-####
    print('Welcome to the game Hangman!')
    print('I am thinking of a word', len(secretWord), 'letters long')
    print('-----------')   
            ####-T-H-E--G-A-M-E--L-O-O-P-####

    while tries > 0:
        
        if isWordGuessed(secretWord, lettersGuessed) == True:
            win = True
            break
        
        print('You have ', tries, ' guesses left')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
    
            if guess in lettersGuessed:
   
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
                print('-----------')

            elif guess in secretWord:
             
                lettersGuessed.append(guess)
                print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
                print('-----------')    
           
            elif guess not in secretWord:
                
                tries -= 1
                lettersGuessed.append(guess)
                print('Oops! that letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                print('-----------')

        else: 
            
            print("Sorry your guess is invalid. Please select 1 letter from a-z")
            print('-----------')
            print(getGuessedWord(secretWord, lettersGuessed))
     
    if win == True:
        
        result = str(gameOverWin)
    else: 
        
        result = str(gameOverLose)

        
    return result
    
if __name__ == '__main__':
    hangman(chooseWord(wordlist))

    