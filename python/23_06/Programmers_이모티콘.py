from collections import Counter

def solution(users, emoticons):
    def DFS(i):
        if i == len(emoticons):
            cnt = Counter(plus)[True]
            if answer[0] == cnt:
                answer[1] = max(answer[1], sum(recent))
            elif answer[0] < cnt:
                answer[0] = cnt
                answer[1] = sum(recent)
        else:
            for discount in [40, 30, 20, 10]:
                tmp = [-1 for _ in range(n)]
                for t in range(n):
                    if not plus[t] and users[t][0] <= discount:
                            tmp[t] = recent[t]
                            recent[t] += emoticons[i] * (100 - discount) // 100
                            if users[t][1] <= recent[t]:
                                plus[t] = True
                                recent[t] = 0
                DFS(i + 1)
                for t in range(n):
                    if tmp[t] != -1:
                        recent[t] = tmp[t]
                        plus[t] = False
                    
    n = len(users)
    answer = [0, 0]
    recent = [0 for _ in range(n)]
    plus = [False for _ in range(n)]
    DFS(0)
    return answer
