def solution(pro, spe):
    answer = []
    
    while True:
        cnt = 0
        for i in range(len(pro)):
            pro[i] += spe[i]
        
        for j in range(len(pro)):
            if pro[0] >= 100:
                pro.pop(0)
                spe.pop(0)
                cnt += 1
        
        if cnt != 0:
            answer.append(cnt)
            cnt = 0
            
        if len(pro) == 0:
            break
        
    return answer