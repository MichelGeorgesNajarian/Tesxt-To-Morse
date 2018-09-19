import sys

def letterToMorse(letterNum):
    morseAlphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--."]
    if letterNum > 64 and letterNum < 910 :
        letterNum -= 65
    elif letterNum > 96 and letterNum < 123:
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
