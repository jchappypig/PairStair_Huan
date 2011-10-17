from unittest import TestCase
from pairStairTable import PairStairTable

__author__ = 'hhuang'

class PairStairTableTest(TestCase):

    def testAddProgrammer(self):
        pairTable = PairStairTable()
        previous_number_of_programmer = len(pairTable.programmerList)
        previous_number_of_pair = len(pairTable.pairList)
        pairTable.addProgrammer("James")
        current_number_of_programmer = len(pairTable.programmerList)
        current_number_of_pair = len(pairTable.pairList)
        self.assertEqual(previous_number_of_programmer + 1, current_number_of_programmer)
        self.assertEqual(previous_number_of_pair + previous_number_of_programmer, current_number_of_pair)

    def testAddPair(self):
        pairTable = PairStairTable()
        programmer1Index = 0
        programmer2Index = 1
        pair = pairTable.getPair(programmer1Index, programmer2Index)
        previous_pair_times = pair.numberOfTimesForPairing;
        pairTable.markPair(programmer1Index, programmer2Index)
        current_pair_times = pair.numberOfTimesForPairing
        self.assertEqual(previous_pair_times + 1, current_pair_times)
