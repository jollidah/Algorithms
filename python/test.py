import random

def sol1(n, m ,recommend):
    import sys
    import heapq
    from collections import defaultdict

    inp = sys.stdin.readline
    # n = int(inp())
    # m = int(inp())
    # recommend = inp().split()
    candidates = dict()
    q = []
    del_cnt = defaultdict(int)
    cnt = 0

    for i in range(m):
        num = recommend[i]
        # print(num)
        if num not in candidates:
            if cnt == n:
                # print(q)
                while del_cnt[(tmp:=heapq.heappop(q)[1])]:
                    del_cnt[tmp] -= 1
                del candidates[tmp]
                cnt -= 1
            heapq.heappush(q, ([1, i], num))
            candidates[num] = [1, i]
            cnt += 1
        else:
            candidates[num][0] += 1
            del_cnt[num] += 1
            heapq.heappush(q, (candidates[num], num))
        # print(candidates)
    return " ".join(map(str, sorted(list(map(int, candidates.keys())))))
    print(*sorted(map(int, candidates.keys())))

def sol2(N, Vote, students):
    # N = int(input()) # 사진틀 개수
    # Vote = int(input()) # 총 추천 회수
    # students = list(map(int, input().split())) # 추천 학생 번호
    picture = [] # 사진틀
    score = [] # 사진틀 인덱스와 매치해서 추천수 저장할 리스트

    for i in range(Vote):
        if students[i] in picture: # 사진틀에 있으면
            for j in range(len(picture)): #이부분 N으로 놓고 계속 틀렸음.. ㅋㅋㅋㅋㅋ
                if students[i] == picture[j]:
                    score[j] += 1 #점수증가
        else: # 사진틀에 없고
            if len(picture) >= N: # 사진틀 꽉차있으면
                for j in range(N):
                    if score[j] == min(score): #가장 작은 점수 찾고
                        del picture[j]
                        del score[j]
                        break #먼저 찾으면 스탑 왜냐면 오래된거일수록 인덱스 앞에 있음
            picture.append(students[i]) #새로운거 뒤에 더해줌
            score.append(1)

    picture.sort()
    return ' '.join(map(str, picture))

while True:
    r1 = random.randrange(1, 4)
    r2 = random.randrange(10, 15)
    r3 = []
    for _ in range(r2):
        r3.append(str(random.randrange(1, 10)))
    if (result1 := sol1(r1, r2, r3)) != (result2:=sol2(r1, r2, list(map(int, r3)))):
        print(r1)
        print(r2)
        print(r3)
        print(result1)
        print(result2)
        break