function solution(n, k) {
    var answer = 0;
    
    if (n>=10) {
        k= k - parseInt(n/10)
    }
    
    if (k>=0) {
        answer = (n*12000)+(k*2000)
    } else {
        answer = (n*12000)
    }
    
    return answer;
}