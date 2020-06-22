# Student: Alvin Tu

import pytest
from lab05 import createWordList

def test_createWordList_0():
    # Example test
    # Write to a file with words in it
    words = ['computer', 'science', 'python']
    outfile = open('test_file_0.txt', 'w')
    for item in words:
	    outfile.write(item +'\n')
    outfile.close()

    # Read the file with words created in it to test if createWordList
    # creates a list of words correctly.
    newlist = createWordList('test_file_0.txt')
    assert(len(newlist) == len(words))

    for i in range(len(words)):
        assert(words[i] == newlist[i])

def test_createWordList_1():
    words = ['alvin', 'winner', 'tu']
    outfile = open('test_file_1.txt', 'w')
    for item in words:
            outfile.write(item +'\n')
    outfile.close()

    newlist = createWordList('test_file_1.txt')
    assert(len(newlist) == len(words))

    for i in range(len(words)):
        assert(words[i] == newlist[i])

def test_createWordList_2():
    words = ['a']
    outfile = open('test_file_2.txt', 'w')
    for item in words:
            outfile.write(item +'\n')
    outfile.close()

    newlist = createWordList('test_file_2.txt')
    assert(len(newlist) == len(words))

    for i in range(len(words)):
        assert(words[i] == newlist[i])
#############################

from lab05 import canWeMakeIt

def test_canWeMakeIt_0():
    assert(canWeMakeIt('ape','pae') == True)

def test_canWeMakeIt_1():
    assert(canWeMakeIt('boon','buoni') == False)

def test_canWeMakeIt_2():
    assert(canWeMakeIt('alvin','ahgdiasdvln') == True)

#############################

from lab05 import getWordPoints
letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4,\
		'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,\
		'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
		's':1, 't':1, 'u':1, 'v':4,	'w':4, 'x':8,\
		'y':4, 'z':10}

def test_getWordPoints_0():
    assert(getWordPoints('ape', letterPoints) == 5)

def test_getWordPoints_1():
    assert(getWordPoints('alvin', letterPoints) == 8)

def test_getWordPoints_2():
    assert(getWordPoints('cat', letterPoints) == 5)

