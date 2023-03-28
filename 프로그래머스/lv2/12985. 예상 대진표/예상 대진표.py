def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        # 1 2 3
        # 47 24 12
        a, b = (a+1)//2, (b+1)//2
        # 24 12 11
    return answer