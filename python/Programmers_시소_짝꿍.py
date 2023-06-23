from collections import defaultdict
from math import comb

def solution(weights):
    answer = 0
    cnt = 1
    tmpD = defaultdict(int)
    ex = -1
    weights.sort()
    for i in range(len(weights)):
        if weights[i] == ex:
            cnt += 1
        elif cnt != 1:
                answer -= 2 * comb(cnt, 2)
                cnt = 1
        for d in [2, 3, 4]:
            tmpD[weights[i] * d] += 1
        ex = weights[i]
    if cnt != 1:
        answer -= 2 * comb(cnt, 2)
        cnt = 1
    
    for v in tmpD.values():
        answer += comb(v, 2)
    return answer
