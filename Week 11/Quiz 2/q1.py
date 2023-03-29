def removeLetters(alist, string):
    d = {}
    ans = []
    for i in range(len(string)):
        d[string[i]] = 0
    for i in range(len(alist)):
        if alist[i] not in d:
            ans.append(alist[i])
    return ans


print(removeLetters(["a", "b", "c", "d"], "abcdefg"))
# []
print(removeLetters(["a", "b", "c", "d"], "abe"))
# ['c', 'd']
print(removeLetters(["a", "p", "l", "b", "p", "e", "c"], "apple"))
# ['b', 'c']


def strToDict(alist):
    d = {}
    for items in alist:
        temp = items.split('=')
        d[temp[0]] = temp[1]
    return d


print(strToDict(["cat=meow", "dog=bark"]))
# {'cat': 'meow', 'dog': 'bark'}
print(strToDict(["brand=ducati", "model=scrambler", "year=2021"]))
# {'brand': 'ducati', 'model': 'scrambler', 'year': '2021'}
