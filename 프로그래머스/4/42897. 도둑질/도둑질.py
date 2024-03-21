def solution(money):

    visit = [0] * len(money)
    novisit = [0] * len(money)
    
    visit[0] = money[0]
    visit[1] = money[0]
    
    novisit[0] = 0
    novisit[1] = money[1]
    
    for i in range(2, len(money)-1):
        visit[i] = max(visit[i - 1], visit[i - 2] + money[i])

    for i in range(2, len(money)):
        novisit[i] = max(novisit[i - 1], novisit[i - 2] + money[i])
    
        
    return max(max(visit), max(novisit))