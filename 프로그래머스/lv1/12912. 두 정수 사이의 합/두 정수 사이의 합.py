def solution(a, b):
    answer = 0
    
    sm = 0
    bi = 0
    
    if a >= b:
        bi = a
        sm = b
    else:
        bi = b
        sm = a
        
    for i in range(sm, bi + 1):
        answer += i
    
    return answer