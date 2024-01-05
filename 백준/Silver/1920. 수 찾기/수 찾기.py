n = int(input())
a = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

dic = {}

for i in find:
    if i not in dic:
        if i in a:
            dic[i] = 1
        else:
            dic[i] = 0
    print(dic[i])