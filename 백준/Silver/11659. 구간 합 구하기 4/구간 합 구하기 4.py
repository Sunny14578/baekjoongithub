import sys

input = sys.stdin.readline

n, m = map(int, input().split())
counts = list(map(int, input().split()))

SUM = [0 for i in range(n+1)]
SUM[0] = counts[0]

for i in range(1, len(counts)):
    SUM[i] += counts[i] + SUM[i-1]

for j in range(m):
    a, b = map(int, input().split())
    
    print(SUM[b-1] - SUM[a-2])