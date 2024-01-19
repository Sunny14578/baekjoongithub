import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

arr.sort()

start = 0
end = arr[-1]

while start <= end:
    mid = (start + end) // 2
    
    s = 0
    for i in arr:
        if i <= mid:
            s += i
        else:
            s += mid
            
    if s <= target:
        start = mid + 1 
    else:
        end = mid - 1
        
print(end)