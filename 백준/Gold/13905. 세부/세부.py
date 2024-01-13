import sys
input=sys.stdin.readline

def Find(x):

    if x!=disjoint[x]:
        disjoint[x]=Find(disjoint[x])
    return disjoint[x]

N,M=map(int,input().split())

S,E=map(int,input().split())

disjoint=[ _ for _ in range(N+1) ]

edge=[]

for i in range(M):

    a,b,c=map(int,input().split())

    edge.append((c,a,b))

edge.sort(key=lambda x:-x[0])

check=[]
for value,x,y in edge:


    x=Find(x)
    y=Find(y)


    if x!=y:
        if x>y:
            disjoint[x]=y
        else:
            disjoint[y]=x

    if Find(S)==Find(E):
        check.append(value)

if check:
    print(max(check))
else:
    print(0)