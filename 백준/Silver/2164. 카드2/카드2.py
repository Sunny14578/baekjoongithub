from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque(range(1, n+1))

while len(q) > 1:
    q.popleft()
    q.rotate(-1)
    
print(q[0])