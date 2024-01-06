from collections import deque
n, k = map(int, input().split())
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