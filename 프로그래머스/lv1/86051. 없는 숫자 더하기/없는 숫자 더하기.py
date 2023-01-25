def solution(numbers):
    answer = 0
    
    lst = [0] * 10
    
    for i in range(len(numbers)):
        lst[numbers[i]] = 1
        
    for j in range(len(lst)):
        if lst[j] == 0:
            answer += j
    
    return answer