n = int(input())
arr = []
for i in range(n):
    a, b = input().split()
    arr.append([int(a), b, i])
    
arr.sort(key=lambda x: (x[0], x[2]))

for i, j, k in arr:
    print(i, j)