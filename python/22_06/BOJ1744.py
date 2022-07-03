import sys

res = 0
n = int(sys.stdin.readline())
posNumList = []         # 양수를 저장할 리스트
negNumList = []         # 음수를 저장할 리스트
zeroNum = 0             # 0의 갯수를 저장할 변수
for _ in range(n):
    data = int(sys.stdin.readline().strip())
    if data < 0:
        negNumList.append(data)
    elif data > 0:
        posNumList.append(data)
    else:
        zeroNum += 1
negLen = len(negNumList)    # 음수 리스트의 길이 (지속적으로 최신화 될 것)
posLen = len(posNumList)    # 양수 리스트의 길이 (지속적으로 최신화 될 것)
negNumList.sort()           # 리스트 정렬(nlogn)
posNumList.sort(reverse=True)
while negLen > 1:
    res += negNumList.pop(0) * negNumList.pop(0)    # 음수에서 절댓값이 가장 큰 두 숫자를 곰해서 더한다
    negLen -= 2
if zeroNum == 0 and negLen == 1:                    # 음수 리스트에서 원소가 하나 남았을 경우 0이 있다면 0을 곱해 0으로 바꾼다
    res += negNumList.pop(0)
while posLen > 1:
    if posNumList[0] > 1 and posNumList[1] > 1:     # 양수 리스트에서 절댓값이 가장 큰 두 원소가 모두 1보다 클 경우엔 두 원소를 곱해서 더한다
        res += posNumList.pop(0) * posNumList.pop(0)
        posLen -= 2
    else:
        res += posNumList.pop(0) + posNumList.pop(0)    # 양수 리스트에서 절댓값이 가장 큰 두 원소중 하나라도 1이라면 각각 res에 더한다
        posLen -= 2
if posLen == 1:
    res += posNumList.pop(0)                            # 양수 리스트에 값이 남아 있다면 그냥 res에 더해버린다
print(res)

# https://www.acmicpc.net/status?from_problem=1&problem_id=1744
