import sys



n = int(sys.stdin.readline())

def myStack(stack, command):
    l = len(stack)
    
    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == '3':
        print(l)
    elif command[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
stack = []

for i in range(n):    
    command = sys.stdin.readline().split()
    myStack(stack, command)