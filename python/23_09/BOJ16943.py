from itertools import permutations
import sys


def Solultion():
    inp = sys.stdin.readline

    a, b = inp().split()
    nList, b = list(a), int(b)

    maxV = -1
    for n in permutations(nList):
        t = "".join(n)
        if t[0] != "0" and (num:= int(t)) < b and maxV < num:
            maxV = num
    return maxV

if __name__ == "__main__":
    print(Solultion())