from pair import Pair

__author__ = 'hhuang'

class PairStairTable(object):
    def __init__(self):
        self.programmerList = []
        self.pairList = []
        self.addProgrammer("Fu Ying")
        self.addProgrammer("Huan Huan")

    def addProgrammer(self, programmer):
        self.programmerList.append(programmer)
        self.AddPairs()


    def AddPairs(self):
        numberOfProgrammers = len(self.programmerList)
        for programmerIndex in range(numberOfProgrammers - 1):
            pair = Pair(programmerIndex, numberOfProgrammers - 1)
            self.pairList.append(pair)

    def getPair(self, programmer1Index, programmer2Index):
        for pair in self.pairList:
            if pair.programmer1Index == programmer1Index and pair.programmer2Index == programmer2Index:
                return pair
        return None

    def markPair(self, programmer1Index, programmer2Index):
        pair = self.getPair(programmer1Index, programmer2Index)
        if not pair == None:
            pair.numberOfTimesForPairing += 1


