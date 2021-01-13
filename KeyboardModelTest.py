import unittest
from KeyboardModel import *


class MyTestCase(unittest.TestCase):

    def test_layout(self):
        testBoard = Keyboard("qwertyuiopasdfghjkl;zxcvbnm,./'")
        assert testBoard.layout == "qwertyuiopasdfghjkl;zxcvbnm,./'"

    def test_hash_positions_to_letters(self):
        testBoard = Keyboard("qwertyuiopasdfghjkl;zxcvbnm,./'")
        for i in range(31):
            assert testBoard.layoutPositionToLetter[i] == "qwertyuiopasdfghjkl;zxcvbnm,./'"[i]

    def test_hash_letters_to_positions(self):
        testBoard = Keyboard("qwertyuiopasdfghjkl;zxcvbnm,./'")
        for i in range(31):
            assert testBoard.layoutLetterToPosition["qwertyuiopasdfghjkl;zxcvbnm,./'"[i]] == i

    def test_layouts_are_mirrored(self):
        testBoard = Keyboard("qwertyuiopasdfghjkl;zxcvbnm,./'")
        for i in range(5):
            assert testBoard.layoutBaseEffort[i] == testBoard.layoutBaseEffort[9-i]
        for i in range(5):
            assert testBoard.layoutBaseEffort[i+10] == testBoard.layoutBaseEffort[19-i]
        for i in range(5):
            assert testBoard.layoutBaseEffort[i+20] == testBoard.layoutBaseEffort[29-i]

    def test_swaptwokeys(self):
        testBoard = Keyboard("qwertyuiopasdfghjkl;zxcvbnm,./'")
        assert testBoard.layout == "qwertyuiopasdfghjkl;zxcvbnm,./'"
        testBoard.swaptwokeys("q", "w")
        assert testBoard.layout == "wqertyuiopasdfghjkl;zxcvbnm,./'"
        assert testBoard.layoutLetterToFinger["w"] == 1
        assert testBoard.layoutLetterToFinger["q"] == 2


if __name__ == '__main__':
    unittest.main()
