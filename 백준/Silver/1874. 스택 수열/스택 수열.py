import sys
input = sys.stdin.readline

stack = []
answer = []
n = int(input())
cnt = 1
check = 1

for i in range(n):
    number = int(input())
    
    while cnt <= number:
        stack.append(cnt)
        answer.append('+')
        cnt+=1
    
    if stack[-1] == number:
        stack.pop()
        answer.append('-')
    else:
        check = 0
        break
        
if check:
    for i in answer:
        print(i)
else:
    print('NO')