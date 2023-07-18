# 단축키 지정

def solution():
    import sys

    inp = sys.stdin.readline
    is_key = set()
    for _ in range(int(inp().rstrip())):
        finish = False
        for i in range(len((inputList := inp().split()))):
            if (tmpKey := inputList[i][0].lower()) not in is_key:
                is_key.add(tmpKey)
                finish = True
                for t in range(i):
                    print(inputList[t], end = " ")
                print("[{}]".format(inputList[i][0]), end = "")
                print(inputList[i][1:], end = " ")
                for t in range(i + 1, len(inputList)):
                    print(inputList[t], end = " ")
                break
        for i in range(len((inputList))):
            if not finish:
                for j in range(1, len(inputList[i])):
                    if (tmpKey := inputList[i][j].lower()) not in is_key:
                        is_key.add(tmpKey)
                        finish = True
                        for t in range(i):
                            print(inputList[t], end = " ")
                        for t in range(j):
                            print(inputList[i][t], end = "")
                        print("[{}]".format(inputList[i][j]), end = "")
                        print(inputList[i][j + 1:], end = " ")
                        for t in range(i + 1, len(inputList)):
                            print(inputList[t], end = " ")
                        break
                    
        if not finish:
            for s in inputList:
                print(s, end = " ")
        print()

if __name__ == "__main__":
    solution()

# https://www.acmicpc.net/problem/1283