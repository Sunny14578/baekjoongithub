import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

cnt = 0
ans = 0
finish = 0

for i in range(n):
    root, left, right = map(int, input().split())
    if left == -1: 
        left = 0
        
    if right == -1:
        right = 0
        
    graph[root].append(left)
    graph[root].append(right)
    
def max_right(node):
    global finish

    finish = node
    
    if graph[node][1]: 
        max_right(graph[node][1])

def inorder(node):
    global cnt, ans
    
    if node == finish:
        ans = cnt
        
    if graph[node][0]:
        cnt += 1
        inorder(graph[node][0])
        cnt += 1
        if node == finish:
            ans = cnt
            
    if graph[node][1]:
        cnt += 1
        inorder(graph[node][1])
        cnt += 1
        
max_right(1)
inorder(1)
print(ans)