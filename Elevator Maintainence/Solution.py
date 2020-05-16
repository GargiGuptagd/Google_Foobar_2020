def answer(l):
    new=[list(map(int,i.strip().split("."))) for i in l]
    new=sorted(new)
    res = [('.'.join(str(ee) for ee in e)) for e in new]
    return res