import KeyboardModel


"""Take in a keyboard, and a string to test on, spit out a score based on how hard it was to type all that"""

def baseEvaluator(keyboard, trainingSet):
    f = open(trainingSet, "r")
    baseDifficultyCounter = 0
    hitsPerKeys = {}
    for i in range(31):
        hitsPerKeys[i] = 0
    for letter in f.read().lower():
        if letter in keyboard.layoutLetterToPosition:
            hitsPerKeys[keyboard.layoutLetterToPosition[letter]] += 1
            baseDifficultyCounter += keyboard.layoutBaseEffort[keyboard.layoutLetterToPosition[letter]]
    return baseDifficultyCounter, hitsPerKeys

def fingerRepetitionEvaluator(keyboard, trainingSet):
    f = open(trainingSet, "r")
    fingerRepetitionCounter = 0
    fingerHitsPerFinger = {}
    repetitionsPerFinger = {}
    for i in range(1, 9):
        fingerHitsPerFinger[i] = 0
        repetitionsPerFinger[i] = 0
    currentFinger = 0
    pastFinger = 0
    for letter in f.read().lower():
        if letter in keyboard.layoutLetterToPosition:
            currentFinger = keyboard.layoutPositionToFinger[keyboard.layoutLetterToPosition[letter]]
            fingerHitsPerFinger[currentFinger] += 1
            if currentFinger == pastFinger:
                fingerRepetitionCounter += 1
                repetitionsPerFinger[currentFinger] += 1
        else:
            currentFinger = 0
        pastFinger = currentFinger
    return fingerRepetitionCounter, fingerHitsPerFinger, repetitionsPerFinger

def textEvaluator(trainingSet):
    f = open(trainingSet, "r")
    letterFrequency = {}
    bigrams = {}
    uniqueletters = set("qwertyuiopasdfghjkl;zxcvbnm,./")
    for i in "qwertyuiopasdfghjkl;zxcvbnm,./":
        letterFrequency[i] = 0
    for letter in f.read().lower():
        if letter in uniqueletters:
            pass
    #TODO: create a table of bigram frequencies, so that we can spit that table out and figure out our best swaps



test1 = "abcdefghijklmnopqrstuvwxyz"
test2 = "qwertyuiopasdfghjkl;zxcvbnm,./"
test3 = "qazwsxedcrfvtgbyhnujmik,ol.p;/"

for i in KeyboardModel.keyboardBundle:
    print(baseEvaluator(i, "TomsCabin.txt"))
    print(fingerRepetitionEvaluator(i, "TomsCabin.txt"))
    print("-------------- "+str(i.layout)+" ---------------")
