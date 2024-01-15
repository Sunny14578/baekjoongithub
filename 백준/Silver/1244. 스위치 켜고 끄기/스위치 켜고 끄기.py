def male(v):
    for k in range(v, n+1, v):
        switch[k] = 1-switch[k] 
    
def female(v):
    switch[v] = 1-switch[v]
    cnt = 1
    answer = 0
    
    for k in range(n//2):
        if v+k > n or v-k < 1:break
        if switch[v-k] == switch[v+k]:
            switch[v-k] = 1-switch[v-k]
            switch[v+k] = 1-switch[v+k]
        else:
            break

n = int(input())
switch = [0] + list(map(int, input().split()))
s = int(input())

l1 = []
for i in range(s):
    gender, value = map(int, input().split())
    l1.append([gender, value])
    
for i in l1:
    g, v = i
    
    if g == 1:
        male(v)
    else:
        female(v)
        
for s in range(1, n+1):
    print(switch[s], end = ' ')
    if s%20 == 0:
        print()