import sys

N, M = map(int, sys.stdin.readline().strip().split())

set1 = set()
set2 = set()

for _ in range(N):
    set1.add(sys.stdin.readline().strip())

for _ in range(M):
    set2.add(sys.stdin.readline().strip())

result = sorted(list(set1 & set2))

print(len(result))

for x in result:
    print(x)