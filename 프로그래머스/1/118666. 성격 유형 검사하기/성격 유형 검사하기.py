def solution(survey, choices):
    
#     p = {'R' : 0, 'T' : 0,
#         'C' : 0, 'F' : 0,
#         'J' : 0, 'M' : 0,
#         'A' : 0, 'N' : 0}
    
#     for i in range(len(survey)):
#         s_list = list(survey[i])
#         print(s_list)
        
#         if choices[i] > 4:
#             p[s_list[1]] += choices[i]-4
#         elif choices[i] < 4:
#             p[s_list[0]] += 4-choices[i]
    score = [3,2,1,0,1,2,3]
    dict = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i,choice in enumerate(choices):
        if choice <= 3:
            dict[survey[i][0]] += score[choice-1]
        elif choice >= 5:
            dict[survey[i][1]] += score[choice-1]
            
    answer = ''
    if dict['R'] >= dict['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dict['C'] >= dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dict['J'] >= dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dict['A'] >= dict['N']:
        answer += 'A'
    else:
        answer += 'N'
        
        
#     li = list(p.items())
#     print(li)
    
#     for i in range(0,8,2):
#         if li[i][1] < li[i+1][1]: 
#             answer += li[i+1][0]
#         else:   
#             answer += li[i][0]
            
#     print(answer)
        
    return answer