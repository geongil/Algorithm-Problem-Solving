def solution(n):
    answer = 0
    
    num = str(n)
    arr = []
    
    for i in num:
        arr.append(i)
    
    arr.sort()
    arr.reverse()
    
    a = ''.join(arr)
    
    answer = int(a)
    
    return answer