def solution(n, words):
    cnt = 0
    who = 0
    stack = []
    
    for i in range(0, len(words)):
        who = (i % n) + 1
        if who == 1:
            cnt += 1
        
        if stack:
            if words[i] in stack:
                return [who, cnt]
            elif words[i][0] == stack[-1][-1]:
                stack.append(words[i])
            elif words[i][0] != stack[-1][-1]:
                return [who, cnt]
        else:
            stack.append(words[i])
    
    return [0, 0]