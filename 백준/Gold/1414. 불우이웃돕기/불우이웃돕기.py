# 모든 컴퓨터가 연결되어야 하고, 연결되는 랜선의 길이가 최소가 되어야한다 ( 크루스칼 알고리즘 )

# 문자를 숫자로 바꿔주는 함수
# ord 함수는 a부터 97이기 때문에 이것을 1로 바꿔주기 위한 작업이 필요하다
def char_to_num(s):
    if 'a' <= s <= 'z':
        return ord(s) - ord('a') + 1    
    elif 'A' <= s <= 'Z':
        return ord(s) - ord('A') + 27
    else:
        return 0
    
# 특정 원소가 속한 집합 찾기
def find(parent, x):
    # 루트 노드를 찾을 때 까지 재귀 호출
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
n = int(input())

graph = []
parent = [i for i in range(n)]
result = 0
total = 0

for i in range(n):
    string = list(input())

    for j in range(n):
        x, y, cost = i, j, char_to_num(string[j])
        
        if i == j:
            total += cost
            continue
        
        if string[j] == '0':
            continue
            
        total += cost
        graph.append((cost, x, y))

graph.sort()
answer = 0

for g in graph:
    cost, x, y = g
    
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        result += cost
        answer += 1

if answer == n-1:
    print(total-result)
else:
    print(-1)