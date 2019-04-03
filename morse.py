import sys

def letterToMorse(letterNum):
    if not ((letterNum > 64 and letterNum < 91) or (letterNum > 96 and letterNum < 123) or letterNum == 32):
        return ''
    elif letterNum > 64 and letterNum < 910 :
        letterNum -= 65
    elif letterNum > 96 and letterNum < 123:
        letterNum -= 97
    elif letterNum == 32:
        return '/'
    else:
        return chr(letterNum)
    return morseAlphabet[letterNum]+"/"

phrase = sys.argv[1]
morseAlphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--."]
morseSentence = ""
for letter in phrase:
    morseSentence += letterToMorse(ord(letter))
    #print ord(letter)

print(morseSentence)
