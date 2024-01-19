import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

start = 0
end = arr[-1]

while start <= end:
    mid = (start+end)//2

    s = 0
    
    for i in arr:
        if i > mid:
            s += i-mid

    if s >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)