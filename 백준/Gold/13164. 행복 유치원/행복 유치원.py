import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = []

for i in range(len(arr)-1):
    t = arr[i+1] - arr[i]
    answer.append(t)

answer.sort()
print(sum(answer[:n-k]))