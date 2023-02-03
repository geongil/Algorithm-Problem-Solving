def solution(left, right):
    answer = 0
    cnt = 0
    for i in range(left, right+1):
        # 여기서 약수개수 확인
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
                
        if cnt % 2:
            answer -= i
            cnt = 0
        else:
            answer += i
            cnt = 0
    
    return answer