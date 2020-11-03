"""This is the model for the keyboard itself. We will be using just the alphabet and punctuation keys for this keyboard.
This means that the total keyboard will span 10x3, no spacebar or number rows"""

"""A basic keyboard will be displayed as below
qwertyuiop
asdfghjkl;
zxcvbnm,./
'
labeled left to right, top to bottom, from 0-30. For example, "a" is at position 10. 30 is for any floater keys, like '

LayoutPositionToFinger defines positions on the keyboard going to what finger should hit them.
QAZ are all hit by the left pinky, which is finger 1 here. Fingers range from 1-8
"""


class Keyboard:
    def __init__(self, layoutString):
        self.layout = layoutString
        self.layoutPositionToLetter = {k: v for k, v in enumerate(layoutString)}   # map the position to the letters assigned
        self.layoutLetterToPosition = {v: k for k, v in enumerate(layoutString)}   # map the letters to their position on the keyboard
        self.layoutLetterToPosition["?"] = self.layoutLetterToPosition["/"]
        self.layoutLetterToPosition["\""] = self.layoutLetterToPosition["'"]
        self.layoutLetterToPosition[":"] = self.layoutLetterToPosition[";"]
        self.layoutBaseEffort = {0: 6,                                # How hard is it to hit the key by default? Set here.
                            1: 3,                                # Note that we penalize pinkies reaching upward
                            2: 3,                                # 30 is reserved for ' " key, or /? on dvorak. Floater
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
                            24: 5,
                            30: 6}
        for i in range(5):                                     # Now we mirror the keys, so left and right difficulty
            self.layoutBaseEffort[9-i] = self.layoutBaseEffort[i]        # match up.
            self.layoutBaseEffort[19-i] = self.layoutBaseEffort[10+i]
            self.layoutBaseEffort[29-i] = self.layoutBaseEffort[20+i]

        #TODO clean this loop up
        self.layoutPositionToFinger = {30: 8}
        for i in range(10):
            if i < 4:
                self.layoutPositionToFinger[i] = 1 + i
                self.layoutPositionToFinger[i+10] = 1 + i
                self.layoutPositionToFinger[i+20] = 1 + i
            elif i == 4:
                self.layoutPositionToFinger[i] = 4
                self.layoutPositionToFinger[i+10] = 4
                self.layoutPositionToFinger[i+20] = 4
            elif i == 5:
                self.layoutPositionToFinger[i] = 5
                self.layoutPositionToFinger[i+10] = 5
                self.layoutPositionToFinger[i+20] = 5
            elif i > 5:
                self.layoutPositionToFinger[i] = i-1
                self.layoutPositionToFinger[i + 10] = i-1
                self.layoutPositionToFinger[i + 20] = i-1

    def showLayout(self):
        asciiLayout = self.layout
        asciiLayout = asciiLayout[:10] + "\n" + asciiLayout[10:20] + "\n" + asciiLayout[20:30] + "   " + asciiLayout[30]
        asciiLayout = asciiLayout.replace("", " ")
        return asciiLayout



qwertyKeyboard = Keyboard("qwertyuiopasdfghjkl;zxcvbnm,./'")
dvorakKeyboard = Keyboard("',.pyfgcrlaoeuidhtns;qjkxbmwvz/")
colemakKeyboard = Keyboard("qwfpgjluy;arstdhneiozxcvbkm,./'")
custom1Keyboard = Keyboard(";,.ypfwlrkaoeiudhtnszxcv'bmgjq/")
custom2Keyboard = Keyboard(";,.ypflwrkaoeiudhtnszxcv'bmgjq/")
#custom3Keyboard = Keyboard(";,.ypfwlrkaoeiudhtnszxcv'bmgjq/")
keyboardBundle = [qwertyKeyboard, dvorakKeyboard, colemakKeyboard, custom1Keyboard, custom2Keyboard]
#custom2Keyboard = Keyboard("")
#custom2Keyboard = Keyboard("")



