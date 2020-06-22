# Student: Alvin Tu
# Make sure to read the comments for each function. 

letterPoints = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2,
                "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1,
                "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1,
                "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}
def createWordList(filename):
    infile = open(filename, 'r')    
    L = infile.read()
    lst_words = L.split()
    infile.close()
    return lst_words

def canWeMakeIt(myWord, myLetters):
    if type(myWord) != str:
        return False
    check1 = list(myWord)
    check2 = list(myLetters)
    for letter in check1:
        if letter in check2:
            make = True
            check2.remove(letter)
        else:
            make = False
            break
    return make

def getWordPoints(myWord, letterPoints):
    totalPoints = 0
    if type(myWord) != str:
        return 0
    for letter in myWord:
        if letter in letterPoints:
            totalPoints += letterPoints[letter]
    return totalPoints


def outputWordPointPairs(pointWordList, myLetters, toFile):
    width = 4 + len(myLetters)
    pairs = open(myLetters + '.txt', 'w+')
    for pair in pointWordList:
        if not toFile:
            print("{0:<{2}}{1}".format(pair[1], pair[0], width))
        if toFile:
            pairs.write("{0:<{2}}{1}".format(pair[1], pair[0], width) + '\n')
    pairs.close()

def scrabbleWords(myLetters):
    pointWordList = []
    wordList = createWordList('wordlist.txt')
    for word in wordList:
        if canWeMakeIt(word, myLetters) == True:
            x = word
            a = getWordPoints(word, letterPoints)
            z = (a, x)
            pointWordList.append(z)
            pointWordList.sort(reverse = True)
    outputWordPointPairs(pointWordList, myLetters, True)
    outputWordPointPairs(pointWordList, myLetters, False)

    
        
    
        
    
