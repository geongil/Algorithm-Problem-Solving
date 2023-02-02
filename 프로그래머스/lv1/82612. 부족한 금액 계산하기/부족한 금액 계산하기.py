def solution(price, money, c):
    answer = 0
    cnt = 0
    
    while True:
        if cnt == c:
            break
        else:
            cnt += 1
            money -= (price * cnt)
        
    if money < 0:
        answer = -(money)
    elif money >= 0:
        answer = 0
    
    return answer