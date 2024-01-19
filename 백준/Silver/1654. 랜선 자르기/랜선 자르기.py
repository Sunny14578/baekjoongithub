import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))
    
start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for i in arr:
        if mid != 0:
            cnt += i // mid
        
    if cnt < m:
        end = mid - 1
    elif cnt >= m:
        start = mid + 1
        
print(end)