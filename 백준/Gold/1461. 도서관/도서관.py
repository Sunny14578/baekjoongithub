import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

plus = []
minus = []
SUM = 0


for i in arr:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)
        
MAX = 0

if plus and minus:
    MAX = abs(minus[0]) if abs(minus[0]) > plus[-1] else plus[-1]
elif plus:
    MAX = max(plus)
else:
    MAX = abs(min(minus))

for i in range(len(plus)-1, -1, -m):
    SUM += plus[i]*2

for j in range(0, len(minus), m):
    SUM += abs(minus[j]*2)
 
print(SUM-MAX)