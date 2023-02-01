def solution(br, ye):
    total = br + ye
    answer = []
    
    for col in range(3, total):
        row = int(total / col)
        
        if (row * col == total) & (row >= col) & ((row - 2) * (col - 2) == ye):
            answer = [row, col]
            break
    
    return answer