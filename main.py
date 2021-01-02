# This is a sample Python script.

LetterWordPairs = {'a': 'alfa',
                   'b': 'bravo',
                   'c': 'charlie',
                   'd': 'delta',
                   'e': 'echo',
                   'f': 'foxtrot',
                   'g': 'golf',
                   'h': 'hotel',
                   'i': 'india',
                   'j': 'juliet',
                   'k': 'kilo',
                   'l': 'lima',
                   'm': 'mike',
                   'n': 'november',
                   'o': 'oscar',
                   'p': 'papa',
                   'q': 'quebec',
                   'r': 'romeo',
                   's': 'sierra',
                   't': 'tango',
                   'u': 'uniform',
                   'v': 'victor',
                   'w': 'whiskey',
                   'x': 'xray',
                   'y': 'yankee',
                   'z': 'zulu',
                   '1': 'wun',
                   '2': 'too',
                   '3': 'tree',
                   '4': 'fow-er',
                   '5': 'fife',
                   '6': 'too',
                   '7': 'seven',
                   '8': 'ait',
                   '9': 'zeero'}

# sierra tango oscar papa - stop
if __name__ == '__main__':
    UserInput = input("[!] ").lower()
    Counter = 0
    for Slovo in UserInput:
        if Slovo[Counter] == ' ':
            print(" ")
        if Slovo in LetterWordPairs.keys():
            print(LetterWordPairs[Slovo[0]])
