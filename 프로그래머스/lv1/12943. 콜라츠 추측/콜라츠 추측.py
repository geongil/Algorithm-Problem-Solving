def solution(num):
    answer = 0
    cnt = 0
    
    if num == 1:
        answer = 0
    
    num1 = num
    
    while num1 != 1:
        if num1 % 2:
            num1 = num1 * 3 + 1
            cnt += 1
        else:
            num1 = num1 / 2
            cnt += 1
                
    if cnt >= 500:
        cnt = -1
    answer = cnt

    
    return answer