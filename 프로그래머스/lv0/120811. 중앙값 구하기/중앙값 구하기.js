function solution(array) {
    var answer = 0;
    
    array.sort(function compare(a, b) {
        return a - b
    })
    
    if (array.length%2) {
        answer = array[parseInt(array.length/2)]
    } 
    
    return answer;
}