function solution(slice, n) {
    var answer = 0;
    
    if (n%slice) {
        answer = parseInt(n/slice) + 1
    } else {
        answer = n / slice
    }
    
    return answer;
}