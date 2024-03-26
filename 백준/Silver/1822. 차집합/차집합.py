import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
c = list(map(int, input().split()))

l.sort()
c.sort()

answer = []

for target in l:
    left = 0
    right = len(c)-1
    
    check = 1
    
    while left <= right:
        mid = int((left + right) / 2)
        
        if c[mid] == target:
            check = 0
            break
        elif c[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    if check:
        answer.append(target)
            
cnt = len(answer) 

if cnt == 0:
    print(0)
else:
    print(len(answer))
    
    for j in answer:
        print(j, end = ' ')