setsize = 10

myset = [[] for _ in range(setsize)]


def add(x):
    myset[x % setsize].append(x)


def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
    return False


def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i], xlist[len(xlist)-1] = xlist[len(xlist)-1], xlist[i]
            xlist.pop()
            return True


if __name__ == '__main__':
    print(myset)
    print(add(myset))