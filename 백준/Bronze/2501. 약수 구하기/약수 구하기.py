n, k = map(int, input().split())

answer = []

for i in range(1, n//2+1):
    if n%i == 0:
        answer.append(i)
answer.append(n)

if len(answer) >= k:
    print(answer[k-1])
else:
    print(0)