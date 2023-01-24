def solution(x):
    answer = True
    num = 0
    
    for i in str(x):
        num += int(i)
        
    if x % num:
        answer = False
    else:
        answer = True
        
    return answer