import unittest
from KeyboardModel import *

testBoard = Keyboard("qwertyuiopasdfghjkl;zxcvbnm,./'")
class MyTestCase(unittest.TestCase):
    #TODO test finger stuff, and display

    def test_layout(self):
        assert testBoard.layout == "qwertyuiopasdfghjkl;zxcvbnm,./'"

    def test_hash_positions_to_letters(self):
        for i in range(31):
            assert testBoard.layoutPositionToLetter[i] == "qwertyuiopasdfghjkl;zxcvbnm,./'"[i]

    def test_hash_letters_to_positions(self):
        #print(testBoard.layoutLetterToPosition.keys())
        for i in range(31):
            assert testBoard.layoutLetterToPosition["qwertyuiopasdfghjkl;zxcvbnm,./'"[i]] == i

    def test_layouts_are_mirrored(self):
        for i in range(5):
            assert testBoard.layoutBaseEffort[i] == testBoard.layoutBaseEffort[9-i]
        for i in range(5):
            assert testBoard.layoutBaseEffort[i+10] == testBoard.layoutBaseEffort[19-i]
        for i in range(5):
            assert testBoard.layoutBaseEffort[i+20] == testBoard.layoutBaseEffort[29-i]


if __name__ == '__main__':
    unittest.main()
