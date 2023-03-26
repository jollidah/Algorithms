import sys 
from queue import PriorityQueue

def calc():
    pass

n = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().split()))
if len(l) == 3:
    print(2 * max(l))
    exit(0)
maxV = 0

p = 1