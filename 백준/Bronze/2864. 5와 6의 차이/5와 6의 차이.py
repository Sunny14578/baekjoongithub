a, b = map(str, input().split(' '))

a_max = ''
a_min = ''

b_max = ''
b_min = ''

for i in a:
    if i == '5':
        a_max += '6'
        a_min += i
    elif i == '6':
        a_max += i
        a_min += '5'
    else:
        a_max += i
        a_min += i
        
for i in b:
    if i == '5':
        b_max += '6'
        b_min += i
    elif i == '6':
        b_max += i
        b_min += '5'
    else:
        b_max += i
        b_min += i
        
print(int(a_min)+int(b_min), int(a_max)+int(b_max))