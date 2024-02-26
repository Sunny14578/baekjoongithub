import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())

p = [i for i in range(n+1)]  # 대표는 자기자신

def union(a, b):
    a = find(a)
    b = find(b) # pa의 대표를 pb로 바꾼다. 기준이 있다면 기준에 맞춰줘야한다.
    
    p[a] = b
    
def find(a): # 대표찾기
    if a == p[a]: # 대표가 자기자신일때
        return a
    
    p[a] = find(p[a]) # 
    return p[a]

for i in range(m):
    c, a, b = map(int, input().split())
    
    if c == 0: # union
        union(a, b)
    else:      # find
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")