n = int(input())
s = list(map(str, input().rstrip()))
star = len(s)*2 - (len(s)-1) - s.count('L')//2
if star >= n:
    print(n)
else:
    print(star)