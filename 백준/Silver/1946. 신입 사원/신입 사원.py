T = int(input())

for i in range(T):    
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split(' '))))
        
    arr.sort()    
    p = arr[0][1]
    cnt = 1

    for i in range(1, len(arr)):
        if p > arr[i][1]:
            cnt+=1
            p = arr[i][1]
    print(cnt)