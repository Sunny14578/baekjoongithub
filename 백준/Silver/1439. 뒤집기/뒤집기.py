s = input()

l = []

start = 0
for i in range(1, len(s)):

    if s[start] == s[i]:
        if i == len(s)-1:
            l.append(int(s[start]))
        pass    
    else:
        l.append(int(s[start]))
        start = i
            
        if i == len(s)-1:
            l.append(int(s[i]))
 
    

        
if l.count(0) > l.count(1):
    print(l.count(1))
else:
    print(l.count(0))