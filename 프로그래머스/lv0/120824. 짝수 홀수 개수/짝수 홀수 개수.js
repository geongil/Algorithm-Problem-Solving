function solution(num_list) {
    var answer = [];
    var a = 0
    var b = 0
    for (i=0; i<num_list.length; i++){
        if (num_list[i]%2) {
            b++
        } else {
            a++
        }
    }
    
    answer.push(a)
    answer.push(b)
    
    return answer;
}