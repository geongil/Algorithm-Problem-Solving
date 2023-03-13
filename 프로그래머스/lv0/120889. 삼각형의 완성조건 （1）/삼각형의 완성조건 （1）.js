function solution(sides) {
    var answer = 2;
    
    sides.sort(function compare(a, b) {
        return a - b
    })
    
    if (sides[sides.length-1] < sides[0]+sides[1]) {
        answer = 1
    }
    
    return answer;
}