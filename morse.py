import sys

def letterToMorse(letterNum):
    morseAlphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--."]
    if letterNum > 65 and letterNum < 90 :
        letterNum -= 65
    elif letterNum > 97 and letterNum < 122:
        letterNum -= 97
    elif letterNum == 32:
        return '/'
    else:
        return chr(letterNum)
    return morseAlphabet[letterNum]+"/"

phrase = sys.argv[1]
morseSentence = ""
for letter in phrase:
    morseSentence += letterToMorse(ord(letter))
    #print ord(letter)

print(morseSentence)
