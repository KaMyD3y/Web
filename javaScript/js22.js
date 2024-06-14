let numbers = [ 10, 20, 30, 40, 80 , 90]
console.log(numbers)
console.log(numbers.length)
console.log(numbers[2])
numbers[3] = 50
console.log(numbers.length)
console.log(numbers)
numbers.length = 7
console.log(numbers.length)
console.log(numbers)
document.getElementById('result').innerHTML = numbers
const firstArray = [ 1, 2, 3, 4]
console.log(firstArray)
const secondArray = [ 'a', 'b' , 'c', 'd'];
console.log(secondArray);
const newArray = firstArray.concat(secondArray);
console.log(newArray);

let oneArray = ['array' ,'bannana' ,1];
let mixString = oneArray.join(";");
let mixString1 = oneArray.join(",");
console.log(mixString);
console.log(mixString1);

let reverseArray = [345];
console.log(reverseArray);
let xArray = reverseArray.join("");
console.log(xArray);
let nowString = xArray.split("").reverse().join("");
let reversedNumber = Number(nowString);
let resultArray = [reversedNumber]
console.log(resultArray)
console.log(typeof resultArray);
console.log(resultArray.length);

let convertArray = ( arrayData , separator) => {
    return arrayData.join(separator);
}
console.log(convertArray(['a' , 'b' , 'd'], ','));
console.log(convertArray(['a' , 'b' , 'd'], '+'));
console.log(convertArray(['a' , 'b' , 'd'], ';'));

let proccesInput = (input) => {
    if (typeof input === 'number'){
        return Number(input.toString().split('').reverse().join(''));
    }
    else if (typeof input === 'string'){
        return input.split('').sort().join('');
    }
    else {
        return 'Invalid input type';
    }
}
console.log(proccesInput(12345));
console.log(proccesInput('mihail'));
