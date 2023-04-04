s = int(input())

SUM = 0
cnt = 0

for i in range(1, s+1):
    SUM+=i
    cnt += 1
    if SUM > s:
        cnt-=1
        break
print(cnt)