def solution(cap, n, deliveries, pickups):
    answer = 0
    di = n - 1
    pi = n - 1
    while di >= 0 and not deliveries[di]:
        di -= 1
    while pi >= 0 and not pickups[pi]:
        pi -= 1
    print(di, pi)
    while di != -1 or pi != -1:
        tmp = cap
        answer += 2 * (max(di, pi) + 1)
        while di != -1:
            if tmp < deliveries[di]:
                deliveries[di] -= tmp
                break
            else:
                tmp -= deliveries[di]
                di -= 1
        tmp = cap
        while pi != -1:
            if tmp < pickups[pi]:
                pickups[pi] -= tmp
                break
            else:
                tmp -= pickups[pi]
                pi -= 1
    return answer
