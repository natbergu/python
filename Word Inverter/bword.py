def bword(word):
    """Returns the word(s), backward."""
    offset = len(str(word)) - 1
    backword = []
    while offset > -1:
        backword.append(str(word)[offset])
        offset -= 1
    return "".join(map(str, backword))

def bword2(word):
    """Returns the word(s), backward.

another (faster? shorter.) way!!"""
    backword2 = []
    for letter in range(1, (len(str(word)) + 1)):
        backword2.append(str(word)[-1 * letter])
    return "".join(map(str, backword2))

def bword3(word):
    """Returns the word(s), backward.

well now that i know this way i look pretty stupid!!"""
    result = list(word)
    result.reverse()
    return "".join(map(str, result))

word = input("word(s) > ")
print(bword(word))
print(bword2(word))
print(bword3(word))
