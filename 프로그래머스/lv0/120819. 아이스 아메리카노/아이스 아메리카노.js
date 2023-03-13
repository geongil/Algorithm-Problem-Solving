function solution(money) {
    var answer = [];
    var a = 0;
    var b = 0;
    
    if (money%5500) {
        a = parseInt(money/5500)
        b = money%5500
    } else {
        a = parseInt(money/5500)
    };
    
    answer.push(a);
    answer.push(b);
    
    return answer;
}