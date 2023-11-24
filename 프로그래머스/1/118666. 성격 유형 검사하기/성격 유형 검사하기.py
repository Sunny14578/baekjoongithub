def solution(survey, choices):
    
    p = {'R' : 0, 'T' : 0,
        'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0,
        'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        s_list = list(survey[i])
        print(s_list)
        
        if choices[i] > 4:
            p[s_list[1]] += choices[i]-4
        elif choices[i] < 4:
            p[s_list[0]] += 4-choices[i]
            
    answer = ''        
            
    if p['R'] >= p['T']:
        answer += 'R'
    else:
        answer += 'T' 
   
    if p['C'] >= p['F']:
        answer += 'C' 
    else:
        answer += 'F' 
        
    if p['J'] >= p['M']:
        answer += 'J' 
    else:
        answer += 'M' 
        
    if p['A'] >= p['N']:
        answer += 'A' 
    else:
        answer += 'M' 
        
    li = list(p.items())
    
    f= ''
    
    for i in range(0,8,2):
        if li[i][1] < li[i+1][1]: f += li[i+1][0]
        else:   f += li[i][0]
        
    return f