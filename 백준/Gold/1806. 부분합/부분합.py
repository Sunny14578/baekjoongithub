import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

prefix = [0] * (n+1)
prefix[1] = l[0]

for i in range(2, n+1):
    prefix[i] = prefix[i-1]+l[i-1]

MIN = n+1
left = 0
right = 1

while left < n:
    dis = prefix[right] - prefix[left]
    
    if dis < m:
        if right < n:
            right += 1
        else:
            left += 1
    else:
        MIN = min(MIN, right-left)
        left += 1
   
if MIN == n+1:
    print(0)
else:
    print(MIN)