if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
firstlar = seclar = -100
for x in a:
    if x > firstlar:
        seclar = firstlar
        firstlar = x
    elif x > seclar and x != firstlar:
        seclar = x
print(seclar)