from Evaluator import *
from KeyboardModel import *

qwertyKeyboard = Keyboard("qwertyuiopasdfghjkl;zxcvbnm,./'")
dvorakKeyboard = Keyboard("',.pyfgcrlaoeuidhtns;qjkxbmwvz/")
dvorakCustomKeyboard = Keyboard("',.pyfgcrlaoeuidhtns;qjkxbmwvz/")
colemakKeyboard = Keyboard("qwfpgjluy;arstdhneiozxcvbkm,./'")
colemakOptimizedKeyboard = Keyboard(";bufpwmlygioeahdtnsr/.,kjqvcxz'")
colemakCustomKeyboard = Keyboard(";bufpwmlygioeahdtnsrcvzkjq,.x/'")
custom1Keyboard = Keyboard(",'uqpfvlrwaoeiydhtns.;zjxbkgmc/")
custom2Keyboard = Keyboard(",'uqpfckrlaoeiygstnh.;zjxbwdvm/")
custom3Keyboard = Keyboard(";.uqjfcdhvoaeiygstnr',zpxbwkml/") #current best, but with rows 7 and 8 swapped
keyboardBundle = [qwertyKeyboard, dvorakKeyboard, dvorakCustomKeyboard, colemakKeyboard, colemakOptimizedKeyboard, colemakCustomKeyboard, custom1Keyboard, custom2Keyboard, custom3Keyboard]

"""This is a testing playground for evaluator. This spits out how good a given layout is."""

for i in keyboardBundle:
    print(i.showLayout())
    print("base difficulty", baseEvaluator(i, "TaleTwoCities.txt"))
    print("repetition", fingerRepetitionEvaluator(i, "TaleTwoCities.txt"))
    print("-------------------------------------------------")
