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
custom3Keyboard = Keyboard(";.uqjfcdhvoaeiygstnr',zpxbwkml/") #current best
keyboardBundle = [qwertyKeyboard, dvorakKeyboard, dvorakCustomKeyboard, colemakKeyboard, colemakOptimizedKeyboard, colemakCustomKeyboard, custom1Keyboard, custom2Keyboard, custom3Keyboard]

"""This is a testing playground for evaluator"""

for i in keyboardBundle:
    print(i.showLayout())
    print("base difficulty", baseEvaluator(i, "TomsCabin"))
    print("repetition", fingerRepetitionEvaluator(i, "TomsCabin"))
    print("-------------------------------------------------")
