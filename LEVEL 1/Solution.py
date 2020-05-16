from collections import Counter
def answer(data,n):
    d=Counter(data)
    return [x for x in d if data.count(x)<=n]