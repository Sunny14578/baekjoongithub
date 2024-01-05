n = int(input())
a = set(map(int, input().split()))
m = int(input())
find = map(int, input().split())

for i in find:
    if i in a:
        print(1)
    else:
        print(0)