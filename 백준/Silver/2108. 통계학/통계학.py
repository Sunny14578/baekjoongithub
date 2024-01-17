import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

def frequency():
    dic = {}

    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1    
            
    l1 = sorted(dic.items(), key = lambda x:(x[1], x[0]), reverse = True)
    MAX = l1[0][1]
    l2 = [i for i in l1 if i[1] == MAX]
    
    if len(l2) > 1:
        return l2[-2][0]
    else:
        return l2[-1][0]

a = round(sum(arr)/len(arr))
b = arr[len(arr)//2]
c = frequency()
d = arr[-1] - arr[0]

print(a)
print(b)
print(c)
print(d)