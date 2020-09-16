def bword(word):
    """returns the word(s), backward!!"""
    offset = len(str(word)) - 1
    backword = []
    while offset > -1:
        backword.append(str(word)[offset])
        offset -= 1
    return "".join(map(str, backword))

def bword2(word):
    """return the word(s), backward another (faster? shorter.) way!!"""
    backword2 = []
    for letter in range(1, (len(str(word)) + 1)):
        backword2.append(str(word)[-1 * letter])
    return "".join(map(str, backword2))

word = input("word(s) > ")
print(bword(word))
print(bword2(word))
