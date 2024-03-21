from collections import deque

answer = 0

def solution(numbers, target):
    visit = [0] * len(numbers)
       
    bfs(numbers, target)

    return answer  

def bfs(numbers, target):
    global answer
    q = deque([[[], 0]])
        
    while q:
        x, depth = q.popleft()
            
        if depth == len(numbers):
            if sum(x) == target:
                answer += 1
        else:
            q.append([x+[numbers[depth]], depth+1])
            q.append([x+[-numbers[depth]], depth+1])
            
#             if depth == len(numbers) and x == target:
#                 cnt += 1
    
#             if depth == len(numbers):
#                 break
                
#             if visit[depth] == 0 :
#                 q.append([x+numbers[depth], depth+1])
#                 q.append([x-numbers[depth], depth+1])
                

                




    