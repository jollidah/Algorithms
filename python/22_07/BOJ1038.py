import sys
from itertools import combinations
n = int(sys.stdin.readline().strip())

comList = []
cnt = 0
for i in range(1, 11):
    for t in combinations(range(0, 10), i):     # range C i 라고 생각하면 편하다
        data = sorted(list(t), reverse=True)
        comList.append(int("".join(map(str, data))))    # 리스트에 있는 숫자들을 정수로 변환하는 식이 인상적이다
        cnt += 1
    if n < cnt:     # 시간을 단축하기 위해 cnt 활용
        break
comList.sort()
try:
    print(comList[n])
except:
    print(-1)   # 예외처리도 알고리즘에서 충분히 활용 가능하다

# https://www.acmicpc.net/problem/1038
