n = int(input())
people = list(map(int, input().split()))

goal = 1
stack = []

while people:
    if people[0] == goal:
        people.pop(0)
        goal += 1
    else:
        stack.append(people.pop(0))
    
    while stack:
        if stack[-1] == goal:
            stack.pop()
            goal += 1
        else:
            break

if stack:
    print('Sad')
else:
    print('Nice')
        