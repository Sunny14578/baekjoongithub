import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
c = list(map(int, input().split()))

l = deque(c)
bot = deque([0]*n)
cnt = 0

def move():
    global cnt
    
    l.rotate() # 컨테이너 옮기기
    bot.rotate()
    bot[n-1] = 0
    
    for i in range(n-2, -1, -1): # 로봇 옮기기           
        if bot[i] == 1 and l[i+1] > 0 and bot[i+1] != 1: # 로봇 옮기기
            bot[i+1], bot[i] = [1, 0]
            l[i+1] -= 1
            
        bot[n-1] = 0

    cnt += 1

while True:
    dur = l.count(0)
    
    if dur >= k:
        break
        
    # 1번에 해당하는 로직 수행
    move()
        
    # 로봇올리기
    if l[0] != 0:
        bot[0] = 1
        l[0] -= 1
    
print(cnt)