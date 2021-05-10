// Find the distinct elements in two arrays.

function findDistinctElement(arr) {

    let nums_set = new Set()
    let result = 0
    for (let i = 0; i < arr.length; i++) {
        if (!nums_set.has(arr[i])) {
            nums_set.add(arr[i])
            result++;
        }
    }

    for (let item of nums_set) {
        console.log(item)
    }

    const numbers = [2,3,4,4,2,3,3,4,4,5,5,6,6,7,5,32,3,4,5]

    console.log([...new Set(arr)])

    console.log(nums_set)
    return nums_set.size;
}

function doUnion(a, n, b, m){
    // code here
    let _a = a;
    for (let i =0; i<m; i++) {
        _a.push(b[i]);
    };
    let _b = [...new Set(_a)]
    return _b.length;
}

let arr = [6, 10, 5, 4, 9, 120, 4, 6, 10];
console.log(findDistinctElement(arr))

console.log(doUnion([1, 1, 2, 2, 3, 3], 6, [8, 9, 7, 6, 5], 5))

function removeSigleStr(s) {
    let mapping = {}
    // s = Array.from(s)
    for (let char of s) {
        if (!mapping[char]) {
            mapping[char] = 1
        } else {
            mapping[char] += 1
        }
    }

    let temp = ""
    for (let i =0; i < s.length; i++) {
        if (mapping[s[i]] > 1) {
            temp += s[i]
        }
    }
    console.log(temp)
    return temp;
}

console.log(removeSigleStr('ghghghreedadfaraarh'))


function allLetter(inputtxt) { 
    var letters = /^[A-Za-z]+$/;
    if(inputtxt.match(letters)) {
        console.log('Your name have accepted : you can try another');
        return true;
    } else {
        console.log('Please input alphabet characters only');
        return false;
    }
}

allLetter('hhj1')

function power(x,y){
     if(y===0){return 1}
     else if (y%2 ===0){
         return power(x,parseInt(y/2))*power(x,parseInt(y/2))
     }else{
          return x*power(x,parseInt(y/2))*power(x,parseInt(y/2))
     }

}