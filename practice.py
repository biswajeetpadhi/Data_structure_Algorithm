

def bub(l1: list):
    n = len(l1)
    for i in range(n):
        flag = True
        for j in range(n-1-i):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
                flag = False
        if flag:
            break
    return l1


if __name__ == "__main__":
    l = ['12', '34', '5']

    t = tuple(map(list, list(set(l))))
    print(t)


    # print(bub([4, 3, 8, 2, 6]))
    a = ["hacker", "earth", "1", "2", "python", "language", "10"]
    b = a[0::2]
    c = a[1::2]
    d = zip(b,c)
    #print(dict(d))

