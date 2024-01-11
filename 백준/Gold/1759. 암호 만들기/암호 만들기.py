def dfs(depth, start, password):
    if depth == l:
        cnt = 0
        for i in password:
            if i in 'aeiou':
                cnt+=1
        if cnt <= 0 or cnt >= l-1:
            return
        print(password)
        return
    
    for i in range(start, c):
        dfs(depth+1, i+1, password + pw[i])

l, c = map(int, input().split(' '))
pw = list(input().split(' '))
pw.sort()

dfs(0, 0, '')