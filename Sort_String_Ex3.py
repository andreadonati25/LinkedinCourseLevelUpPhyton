def SortString(text):
    words = ''.join(sorted(text.split(), key=str.casefold))
    return words

print(SortString('string of words'))
print(SortString('banana ORANGE apple'))