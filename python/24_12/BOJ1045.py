import sys

def solution():
    inp = sys.stdin.readline
    n, m = map(int, inp().split())
    dicts, max_cnt, = dict(), 0
    for _ in range(n):
        inp_str = inp().rstrip()
        cnt = inp_str.count("0")
        max_cnt = max(max_cnt, cnt)
        if inp_str in dicts:
            dicts[inp_str][1] += 1
        else:
            dicts[inp_str] = [cnt, 1]

    k = int(inp())
    items = sorted(list(dicts.values()), key=lambda x: x[1], reverse=True)
    possible = range(k % 2, k + 1, 2)
    for item in items:
        if item[0] in possible:
            print(item[1])
            exit(0)
    print(0)

if __name__ == "__main__":
    solution()
