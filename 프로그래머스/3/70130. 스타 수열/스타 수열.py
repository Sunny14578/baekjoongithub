def solution(a):
    answer = -1
    dic = {}
    
    for i in a:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
    
    for k in dic.keys():
        
        if dic[k] <= answer:
            continue
    
        idx = 0
        cnt = 0
       
        while idx < len(a)-1:
            
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue
            
            cnt += 1
            idx += 2
        
        answer = max(cnt, answer)
        
    if answer == -1:
        return 0
    else:
        return answer*2


              