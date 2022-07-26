import sys

d1 = sys.stdin.readline().strip()
d2 = sys.stdin.readline().strip()
LCSTable = [[0 for _ in range(len(d1) + 1)] for _ in range(len(d2) + 1)]    # LCS를 저장할 2차 배열이다
for i in range(1, len(d2) + 1):
    for p in range(1, len(d1) + 1):
        if d2[i - 1] == d1[p - 1]:
            LCSTable[i][p] = LCSTable[i - 1][p - 1] + 1
        else:
            LCSTable[i][p] = max(LCSTable[i - 1][p], LCSTable[i][p - 1])
print(max(max(LCSTable)))
ptr1, ptr2 = len(d2), len(d1)
res = []
while LCSTable[ptr1][ptr2]:
    if LCSTable[ptr1][ptr2] == LCSTable[ptr1 - 1][ptr2]:
        ptr1 -= 1
    elif LCSTable[ptr1][ptr2] == LCSTable[ptr1][ptr2 - 1]:
        ptr2 -= 1
    else:
        res.insert(0, d1[ptr2 - 1])     # - 1 실수 조심
        ptr1 -= 1
        ptr2 -= 1
for elem in res:
    print(elem, end="")
# LCS 참고 자료 -> https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
# https://www.acmicpc.net/problem/9252
