n = int(input())

l1 = list(map(int, input().split(' ')))
l2 = list(map(int, input().split(' ')))

l3 = l2.copy()
l3.sort()
l1.append(0)

money = 0
mini = l2[0]
cnt = 0

for i in range(0, len(l2)):
    if mini > l2[i]:
        mini = l2[i]
    
    money += (mini * l1[cnt])
    cnt+=1
        
print(money)