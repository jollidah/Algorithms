# 걷는 건 귀찮아

import sys

inp = sys.stdin.readline
n, m = map(int, inp().split())
rickshaws = list(map(int, inp().split()))
dist = list(map(int, inp().split()))
end = dist[0] + rickshaws[0]
tmpEnd = end
cnt = 0
# 시작하자마자 끝난 경우 예외 처리
if end >= m:
    print(0)
    exit(0)

for i in range(1, n):
    s = rickshaws[i]
    if s > tmpEnd:  # 닿을 수 없는 경우
        print(-1)
        break
    if s > end: # 업데이트
        cnt += 1
        end = tmpEnd
    tmpEnd = max(tmpEnd, dist[i] + s)
    if tmpEnd >= m:
        print(cnt + 1)
        break
else:
    print(-1)

# https://www.acmicpc.net/problem/20928