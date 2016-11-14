"""

Unique word from training set:
If there is only one word that is not in the RockYou training set, 
that is most likely the real password. 
Also, if there is only one that is in the 
RockYou training set, that is the real password
Frequency dictionary of word in sweetwords

"""

sweetWords = [["we", "wah", "jah"], ["ge", "wah","way"], ["gree", "green", "grot"]]
rockYou = []
uniqueList = []
FREQ_THRESH = 5



PATH_TO_FILE = "/Users/divinity/security/rockyou-withcount.txt"


for line in open(PATH_TO_FILE,"r").readlines():
    word = line.split(" ")
    rockYou.append((word[-1]).rstrip("\n"))


def makeSweetList(sweetWords):
    """
    Flattens array into list
    """
    sList = []
    for i in range(len(sweetWords)):
        for j in range (len(sweetWords[0])):
            sList.append(sweetWords[i][j])
    return sList


def wordRock(word):
    return word in rockYou


def uniqueWords(sweetList): 
    unique = set()
    for word in sweetList:
        unique.add(word)
    uList = list(unique)
    
    return uList

def makeDict(sweetList):
    sDict = dict()
    for word in sweetList:
        if word in sDict:
            sDict[word] += 1
        else:
            sDict[word] = 1
    
    return sDict
    


def pPassWords(sweetDict, n):
    pPass = []
    for key in sweetDict:
        if sweetDict[key] < n:
            pPass.append(key)
    return pPass

sweetList = makeSweetList(sweetWords)
uniqueList = uniqueWords(sweetList)
sweetDict = makeDict(sweetList)
probPass = pPassWords(sweetDict, FREQ_THRESH)

notRockYou = []
filtRockYou = []

for word in uniqueList:
    for rock in rockYou:
        if word.lower() != rock.lower():
            notRockYou.append(word)
        else:
            filtRockYou.append(word)



