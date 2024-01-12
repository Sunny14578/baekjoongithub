from collections import deque

n = int(input())
par = list(map(int, input().split()))
del_node = int(input())

graph = [[] for _ in range(n)]
visit = [0] * n 

nodes = [[idx, val] for idx, val in enumerate(par)]
root = par.index(-1)

for i in nodes:
    u, v = i

    graph[v].append(u)

visit[root] = 1
visit[del_node] = 1

if del_node == root:
    print(0)
    exit()

def bfs():
    answer = 0
    
    q = deque([root])
    
    while q:
        check = 0
        val = q.popleft()
        
        if graph[val]:
            for i in graph[val]:
                if visit[i] == 0:
                    visit[i] = 1
                    q.append(i)
                    check = 1

                    
        if check == 0:
            answer += 1
    return answer

print(bfs())