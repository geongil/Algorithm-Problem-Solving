from collections import deque

def solution(n, arr1, arr2):
    answer = []
    
    mat = [''] * n 
    
    for i in range(n):
        # 2진법 변경
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]
    
    # 빈 0값 넣어주기
    for j in range(n):
        if n - len(arr1[j]) != 0:
            arr1[j] = ('0' * (n - len(arr1[j]))) + arr1[j]
        
        if n - len(arr2[j]) != 0:
            arr2[j] = ('0' * (n - len(arr2[j]))) + arr2[j]
    
    # 둘 합치기
    for k in range(n):
        for l in range(n):
            if arr1[k][l] == '1' or arr2[k][l] == '1':
                mat[k] += '#'
            
            else:
                mat[k] += ' '
                
            
            
    answer = mat
    
              
    return answer