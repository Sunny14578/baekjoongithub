import sys

input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))

SUM = []
SUM.append(sum(l[:k]))

for i in range(n-k):
    SUM.append(SUM[i] - l[i] + l[k+i])
    
print(max(SUM))