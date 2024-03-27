import sys
input = sys.stdin.readline

n, h = map(int, input().split(" "))

down = [0] * h  
up = [0] * h 

for i in range(n):
    end=int(input())-1
    
    if i%2==0: 
        down[end]+=1
    else: 
        up[end]+=1
        
for i in range(h-2, -1, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]    
    
down.reverse()

answer = []
for j in range(len(down)):
    answer.append(down[j] + up[j]) 

print(min(answer), answer.count(min(answer)))
