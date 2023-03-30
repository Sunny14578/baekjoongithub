n, t = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

cnt = 0

if t == 1:
    cnt += len(arr)
    
    for i in range(len(arr)-3):
        if arr[i] == arr[i+1] and arr[i+1] == arr[i+2] and arr[i+2] == arr[i+3]:
            cnt += 1
            
if t == 2:
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            cnt+=1
            
if t == 3:
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] and arr[i+1]+1 == arr[i+2]:
            cnt+=1

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]+1:
            cnt+=1
            
if t == 4:
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1]+1 and arr[i+1] == arr[i+2]:
            cnt+=1
    
    for i in range(len(arr)-1):
        if arr[i]+1 == arr[i+1]:
            cnt+=1
            
if t == 5:
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
            cnt+=1
            
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]+1:
            cnt+=1
     
    for i in range(len(arr)-1):
        if arr[i]+1 == arr[i+1]:
            cnt+=1
            
    for i in range(len(arr)-2):
        if arr[i] == arr[i+2] and arr[i] == arr[i+1]+1:
            cnt+=1
            
if t == 6:
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
            cnt+=1
            
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            cnt+=1            

    for i in range(len(arr)-2):
        if arr[i]+1 == arr[i+1] and arr[i+1] == arr[i+2]:
            cnt+=1
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]+2:
            cnt+=1
            
if t == 7:

    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
            cnt+=1
            
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            cnt+=1            

    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]+1:
            cnt+=1
    
    for i in range(len(arr)-1):
        if arr[i]+2 == arr[i+1]:
            cnt+=1

print(cnt)