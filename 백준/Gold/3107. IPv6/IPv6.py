s = input()
s = s.split(":")
    
check = False
    
answer = []
    
for i in s:
    if i == "" and not check:
        answer += ['0000' for _ in range(8 - len(s) + 1)]
        check = True
    else:
        answer.append(i.zfill(4))
            
print(":".join(answer))