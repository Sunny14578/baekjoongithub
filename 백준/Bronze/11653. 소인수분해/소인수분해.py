n = int(input())
a = 2
while a <= int(n ** 0.5):  
    if n % a == 0:    
        print(a)    
        n //= a  
    else:    
        a += 1
if n > 1:  
    print(n)
