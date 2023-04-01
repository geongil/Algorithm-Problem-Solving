def solution(arr):
    a = min(arr)
    
    for i in range(len(arr)):
        if arr[i] == a:
            arr.pop(i)
            break
            
    if len(arr):
        return arr
    else:
        return [-1]