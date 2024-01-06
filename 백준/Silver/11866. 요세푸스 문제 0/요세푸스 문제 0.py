from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
q = deque(range(1, n+1))

answer = []

while q:
    q.rotate(-(k-1))
    answer.append(q.popleft())

print('<', end = '')

for i in range(len(answer)):
    if i == len(answer)-1:
        print(answer[i], end = '>')
    else:
        print(answer[i], end = ', ')