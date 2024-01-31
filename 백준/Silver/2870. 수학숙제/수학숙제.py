import sys

n = int(sys.stdin.readline())

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

res = []

for _ in range(n):
    m = list(map(str, sys.stdin.readline().strip("\n")))
    temp = []
    cnt = ""

    for i in m:
        if i in nums:
            cnt += i

        else:
            if cnt:
                temp.append(int(cnt))
                cnt = ""

    if cnt:
        temp.append(int(cnt))


    res += temp

res.sort()
for j in res:
    print(j)