# 팀배분

import sys

def DFS(person, is_blueteam):
    if is_blueteam:
        blue_team.append(person)
    else:
        red_team.append(person)
    for hate in ban[person]:
        if hate in candidate:
            candidate.remove(hate)
            DFS(hate, not is_blueteam)

inp = sys.stdin.readline
n = int(inp())
blue_team = []
red_team = []
ban = [[]] + [list(map(int, inp().split()))[1:] for _ in range(n)]
candidate = set(range(1, n + 1)) # set
while candidate:
    c = candidate.pop()
    DFS(c, True)    

blue_team.sort()
red_team.sort()
print(len(blue_team))
print(*blue_team)
print(len(red_team))
print(*red_team)

# https://www.acmicpc.net/problem/1953