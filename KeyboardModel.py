"""This is the model for the keyboard itself. We will be using just the alphabet and punctuation keys for this keyboard.
This means that the total keyboard will span 10x3, no spacebar or number rows"""

"""A basic keyboard will be displayed as below
qwertyuiop
asdfghjkl;
zxcvbnm,./
labeled left to right, top to bottom, from 0-29. For example, "a" is at position 10
"""


class Keyboard:
    def __init__(self, layoutString):
        self.layout = layoutString
        self.layoutPositionToLetter = {k: v for k, v in enumerate(layoutString)}   # map the position to the letters assigned
        self.layoutLetterToPosition = {v: k for k, v in enumerate(layoutString)}   # map the letters to their position on the keyboard
        self.layoutBaseEffort = {0: 6,                                # How hard is it to hit the key by default? Set here.
                            1: 3,                                # Note that we penalize pinkies reaching upward
                            2: 3,
                            3: 3,
                            4: 4,
                            10: 0,
                            11: 0,
                            12: 0,
                            13: 0,
                            14: 2,
                            20: 3,
                            21: 5,
                            22: 6,
                            23: 3,
                            24: 5}
        for i in range(5):                                     # Now we mirror the keys, so left and right difficulty
            self.layoutBaseEffort[9-i] = self.layoutBaseEffort[i]        # match up.
            self.layoutBaseEffort[19-i] = self.layoutBaseEffort[10+i]
            self.layoutBaseEffort[29-i] = self.layoutBaseEffort[20+i]


