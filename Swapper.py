from KeyboardModel import *
from Evaluator import *
import copy

"""The goal of this swapper is to run several evaluations and swap keys to optimize.

Input: a keyboard, a key to optimize, and then something to optimize for.
Output: suggests a single swap
TODO: change keyboard model so that it handles swaps by changing all things. Currently / and ? don't get updated"""

def swapKeyForRepetitions(keyboard, flexKey):
    uniqueKeys = keyboard.layout
    uniqueKeys = uniqueKeys.replace(flexKey, "")
    swapchange = {}
    finger1 = keyboard.layoutLetterToFinger[flexKey]
    for i in uniqueKeys:
        #print(i)
        newKeyboard = copy.deepcopy(keyboard)
        finger2 = keyboard.layoutLetterToFinger[i]
        if finger1 != finger2:
            repetitions1, evaluationsPerFinger, hitsPerFinger1 = fingerRepetitionEvaluator(newKeyboard, "TomsCabin")
            preSwapEvaluation1, preSwapEvaluation2 = evaluationsPerFinger[finger1], evaluationsPerFinger[finger2]
            newKeyboard.swaptwokeys(flexKey, i)

            repetitions2, evaluationsPerFinger2, hitsPerFinger2 = fingerRepetitionEvaluator(newKeyboard, "TomsCabin")
            postSwapEvaluation1, postSwapEvaluation2 = evaluationsPerFinger2[finger1], evaluationsPerFinger2[finger2]
            swapchange[i] = (i, repetitions1 - repetitions2, finger1, preSwapEvaluation1, postSwapEvaluation1, finger2, preSwapEvaluation2, postSwapEvaluation2)
            if swapchange[i][1] >= -50:
                #print(newKeyboard.layout, keyboard.layout)
                print(i, swapchange[i])

    #return swapchange


custom2Keyboard = Keyboard(";.uqjfcdhvoaeiygstnr',zpxbwkml/")
print(custom2Keyboard.layout)
print(custom2Keyboard.showLayout())
print(swapKeyForRepetitions(custom2Keyboard, "g"))
for i in custom2Keyboard.layout:
    print(i, swapKeyForRepetitions(custom2Keyboard, i))