import sys

input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

MIN = price[0]
money = 0

for i in range(len(dis)):
    if MIN > price[i]:
        MIN = price[i]
    
    money += MIN * dis[i]
print(money)