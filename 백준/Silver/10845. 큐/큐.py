import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    com = list(input().split())
    
    if len(com) == 2:
        arr.append(com[1])
    else:
        if com[0] == 'pop':
            if arr:
                print(arr.pop(0))
            else:
                print(-1)
        elif com[0] == 'size':
            print(len(arr))
        elif com[0] == 'empty':
            if arr:
                print(0)
            else:
                print(1)
        elif com[0] == 'front':
            if arr:
                print(arr[0])
            else:
                print(-1)
        elif com[0] == 'back':
            if arr:
                print(arr[-1])
            else:
                print(-1)