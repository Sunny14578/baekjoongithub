n, m = map(int, input().split())

dic = {}

for i in range(n):
    url, pw = input().split()
    
    if url not in dic:
        dic[url] = pw

for j in range(m):
    url = input()
    
    print(dic[url])