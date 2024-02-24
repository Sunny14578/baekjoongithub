x = int(input())
n = int(input())

SUM = 0
for i in range(n):
    a, b = map(int, input().split())
    SUM += a*b
    
if x == SUM:
    print('Yes')
else:
    print('No')