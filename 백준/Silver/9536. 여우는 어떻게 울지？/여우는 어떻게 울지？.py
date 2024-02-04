n = int(input())


for i in range(n):
    first = input().split(' ')
    
    while True:
        s = input()
        
        if s == 'what does the fox say?':
            for i in first:
                print(i, end = ' ')
            break
        
        
        remove = s.split('goes ')
        
        first = [x for x in first if x != remove[1]]