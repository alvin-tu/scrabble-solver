# Alvin Tu

# set points for letters
letterPoints = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2,
                "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1,
                "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1,
                "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}

# creates a list of words from a file of words
def createWordList(filename):
    infile = open(filename, 'r')    
    L = infile.read()
    lst_words = L.split()
    infile.close()
    return lst_words

# check if the letters can create the word
def canWeMakeIt(myWord, myLetters):
    if type(myWord) != str:
        return False
    check1 = list(myWord)
    check2 = list(myLetters)

    #iterate through a list of letters from the word and the given letters
    for letter in check1:
        if letter in check2:
            make = True
            check2.remove(letter)
        else:
            make = False
            break
    return make

# match the words to the given points
def getWordPoints(myWord, letterPoints):
    totalPoints = 0
    if type(myWord) != str:
        return 0
    for letter in myWord:
        if letter in letterPoints:
            totalPoints += letterPoints[letter]
    return totalPoints

# prints out the word that can be created as well as the points worth
def outputWordPointPairs(pointWordList, myLetters, toFile):
    width = 4 + len(myLetters)
    pairs = open(myLetters + '.txt', 'w+')
    for pair in pointWordList:
        if not toFile:
            print("{0:<{2}}{1}".format(pair[1], pair[0], width))
        if toFile:
            pairs.write("{0:<{2}}{1}".format(pair[1], pair[0], width) + '\n')
    pairs.close()

# function that takes in letters and outputs all possible scrabble combination
# with point values
def scrabbleWords(myLetters):
    pointWordList = []

    # opens text file and creates list of words
    wordList = createWordList('wordlist.txt')

    # iterates through each word in the list
    for word in wordList:
        #checks if the word can be made
        if canWeMakeIt(word, myLetters) == True:
            x = word
            a = getWordPoints(word, letterPoints)
            z = (a, x)
            # appends tuples of word and points to a list
            pointWordList.append(z)
            pointWordList.sort(reverse = True)
    # writes the words to a file
    outputWordPointPairs(pointWordList, myLetters, True)
    # prints out the combinations for scrabble
    outputWordPointPairs(pointWordList, myLetters, False)

    
        
    
        
    
