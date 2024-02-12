import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
l2 = set(li)

answer = list(l2)
answer.sort()

for i in answer:
    print(i, end = ' ')