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

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m)]
    
    edges = [] # 간선을 담을 리스트
    result = 0 # 최종 비용을 담을 변수
    
    for _ in range(n):
        x, y, cost = map(int, input().split())
        edges.append((cost, x, y))
    edges.sort()

    for edge in edges:
        cost, x, y = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find(parent, x) != find(parent, y):
            union(parent, x, y)
        else:
            result += cost
        
    print(result)