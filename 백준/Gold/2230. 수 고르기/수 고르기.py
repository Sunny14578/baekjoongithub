import sys
input = sys.stdin.readline

n, m = map(int, input().split())

l = []
for i in range(n):
    l.append(int(input()))
    
l.sort()

MIN = 2000000001

left, right = 0, 1

while left < n and right < n:
    minus = l[right] - l[left]
    
    if m > minus:
        right += 1
        continue
    left += 1
    
    MIN = min(MIN, minus)
print(MIN)