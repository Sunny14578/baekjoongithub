while True:
    a = input()
    stack = []
    
    if a == "." :
        break
    
    for i in a:
        if i == '(' or i == ')' or i == '[' or i == ']':
            if stack:
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                    continue
                elif stack[-1] == '[' and i == ']':
                    stack.pop()
                    continue
            stack.append(i)
    
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')