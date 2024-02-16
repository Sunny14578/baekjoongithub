import sys
input = sys.stdin.readline

n = int(input())

l1 = []

for i in range(n):
    x, y = map(int, input().split())
    l1.append([y, x])
    
l1.sort()

for y, x in l1:
    print(x, y)