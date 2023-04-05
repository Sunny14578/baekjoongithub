t = int(input())

arr = []

for i in range(t):
    arr.append(input())

dic = {}

for i in arr:
    l = len(i)
    for j in i:
        if j not in dic:
            dic[j] = 10**(l-1)
            l-=1
        else:
            dic[j] += 10**(l-1)
            l-=1

arr2 = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

cnt = 9

SUM = 0
for i in arr2:
    SUM += arr2[i] * cnt
    cnt -= 1
    
print(SUM)