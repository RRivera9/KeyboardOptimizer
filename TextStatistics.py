class TextStatistics:
    def __init__(self, pathToText):
        f = open(pathToText, "r")
        letterFrequency = {}
        bigrams = {}
        uniqueletters = set("qwertyuiopasdfghjkl;zxcvbnm,./")
        bigramList = []
        letterFrequencyList = []
        for i in "qwertyuiopasdfghjkl;zxcvbnm,./":
            letterFrequency[i] = 0
        pastLetter = -1  # set to -1 to make the oncoming code skip the first letter
        for letter in f.read().lower():
            if letter in uniqueletters:
                letterFrequency[letter] += 1
                if pastLetter != -1:
                    bigram = pastLetter + letter
                    if bigram in bigrams:
                        bigrams[bigram] += 1
                    else:
                        bigrams[bigram] = 0
                pastLetter = letter
            else:
                pastLetter = -1
        for i in bigrams:
            bigramList.append((i, bigrams[i]))
        for i in letterFrequency:
            letterFrequencyList.append((i, letterFrequency[i]))
        self.uniqueLetters = uniqueletters
        self.bigrams = bigrams
        self.letterFrequency = letterFrequency
        self.bigramList = sorted(bigramList, key=lambda x: x[1])
        self.letterFrequencyList = sorted(letterFrequencyList, key=lambda x: x[1])

    def getBigramList(self):
        return self.bigramList

    def getLetterFrequencyList(self):
        return self.letterFrequencyList

    def getBigramDictionary(self):
        return self.bigrams

    def getLetterFrequencyDictionary(self):
        return self.letterFrequency

    def getBigramsByLetter(self, letterToCheckFor):
        letterSpecificBigramDictionary = {}
        letterSpecificBigramList = []
        for i in self.uniqueLetters:
            letterSpecificBigramDictionary[i] = 0
        for i in self.bigramList:
            if letterToCheckFor in i[0]:
                remainingLetter = i[0].replace(letterToCheckFor, "")
                if remainingLetter != "":
                    letterSpecificBigramDictionary[remainingLetter] += i[1]
                else:
                    letterSpecificBigramDictionary[letterToCheckFor] = i[1]
        for i in letterSpecificBigramDictionary:
            letterSpecificBigramList.append((i, letterSpecificBigramDictionary[i]))
        letterSpecificBigramList = sorted(letterSpecificBigramList, key=lambda x: x[1])
        return letterToCheckFor, letterSpecificBigramList


tomsCabin = TextStatistics("TomsCabin")
print(tomsCabin.getLetterFrequencyList())
#print(tomsCabin.getBigramList())
print(tomsCabin.getBigramsByLetter("e"))
print(tomsCabin.getBigramsByLetter("u"))
print(tomsCabin.getBigramsByLetter("a"))
print(tomsCabin.getBigramsByLetter("o"))
print(tomsCabin.getBigramsByLetter("q"))
print(tomsCabin.getBigramsByLetter("c"))
