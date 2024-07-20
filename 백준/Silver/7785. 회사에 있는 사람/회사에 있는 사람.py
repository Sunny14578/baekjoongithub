n = int(input())
dic = {}

for _ in range(n):
    name, l = input().split()
    dic[name] = l
    if l == "leave":
        del dic[name]


d = sorted(dic.items(), reverse=True)
dic = dict(d)


for key in dic.keys():
    print(key)