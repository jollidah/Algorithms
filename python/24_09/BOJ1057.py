import sys

def main():
    inp = sys.stdin.readline
    _, a, b = map(int, inp().split())
    a, b, cnt = a - 1, b - 1, 1

    while True:
        a = a // 2
        b = b // 2
        if a == b:
            break
        cnt += 1
    print(cnt)
if __name__ == "__main__":
    main()
