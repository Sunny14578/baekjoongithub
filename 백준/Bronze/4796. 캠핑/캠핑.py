cnt = 1

while True:
    L, P, V = map(int, input().split(' '))
    
    if L == 0 and P == 0 and V == 0:
        break
    
    result = 0
    if V%P <= L:
        result = (V//P * L) + (V%P)

    else:
        result = (V//P * L) + L

        
    print(f'Case {cnt}: {result}')
    cnt +=1