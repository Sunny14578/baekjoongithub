n = int(input())

top = list(map(int, input().split(' ')))

answer = [0] * n
stack = []

for idx, val in enumerate(top):
    while stack:
        if stack[-1][1] < val:
            stack.pop()
        else:
            answer[idx] = stack[-1][0]+1
            break
        
    stack.append([idx, val])
print(' '.join(map(str, answer)))