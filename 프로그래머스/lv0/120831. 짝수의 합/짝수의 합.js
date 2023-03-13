function solution(n) {
    var answer = 0;
    var step;
    for (step = 1; step<=n; step++) {
        if (step%2 == 0) {
            answer += step
            }
    };
    
    return answer;
}