from collections import deque
import sys

n = int(input())
q = deque()

for i in range(n):
    com = list(map(int, sys.stdin.readline().strip().split()))
    leng = len(q)
    if com[0] == 1:
        q.appendleft(com[1])
    elif com[0] == 2:
        q.append(com[1])
    elif com[0] == 3:
        print(q.popleft() if leng else -1)
    elif com[0] == 4:
        print(q.pop() if leng else -1)
    elif com[0] == 5:
        print(len(q))
    elif com[0] == 6:
        print(0 if leng else 1)
    elif com[0] == 7:
        print(q[0] if leng else -1)
    elif com[0] == 8:
        print(q[-1] if leng else -1)