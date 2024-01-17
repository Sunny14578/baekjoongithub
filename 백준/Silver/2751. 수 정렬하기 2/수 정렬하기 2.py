import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

def merge(arr):

    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low = merge(arr[:mid])
    high = merge(arr[mid:])
    
    merge_arr = []
    l = h = 0
    
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            merge_arr.append(low[l])
            l += 1
        else:
            merge_arr.append(high[h])
            h += 1
            
    merge_arr += low[l:]
    merge_arr += high[h:]
    return merge_arr

answer = merge(arr)

for i in answer:
    print(i)