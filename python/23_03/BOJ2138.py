# 전구와 스위치

import sys
import copy

def switch(s, n):
    for i in range(3):
        if s[n - 1 + i] == "0":
            s[n - 1 + i] = "1"
        else:
            s[n - 1 + i] = "0"

sys.stdin.readline()
s1 = list("0" + sys.stdin.readline().strip() + "0")
s2 = copy.deepcopy(s1)
ans = list(sys.stdin.readline().strip())
res = 1e9

# 첫 번째 스위치 누른 경우
cnt = 1
ptr = 2
switch(s1, 1)
while(ptr < len(s1) - 1):
    if s1[ptr - 1] != ans[ptr - 2]:
        cnt += 1
        switch(s1, ptr)
    ptr += 1
if s1[-2] == ans[-1]:
    res = min(res, cnt)

<<<<<<< HEAD
# 두 번째 스위치 누른
=======
# 첫 번째 스위치를 누르지 않은 경우
>>>>>>> ad513d3a853dbdb214beb1cd3816a8b8e8fdea49
cnt = 0
ptr = 2
while(ptr < len(s2) - 1):
    if s2[ptr - 1] != ans[ptr - 2]:
        cnt += 1
        switch(s2, ptr)
    ptr += 1
if s2[-2] == ans[-1]:
    res = min(res, cnt)

print(res if res != 1e9 else -1)

# https://www.acmicpc.net/problem/2138
