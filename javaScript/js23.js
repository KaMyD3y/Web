// let check = (i,lab=[30 , 40, 20, 10, 5]) => {
//     do { console.log (lab[i]); 
//         i++;
//     } while (i < lab.length);
// }
// check(0)
// let checkOther = (x,number=[30 , 40, 20, 10, 5]) => {
//     while (x < number.length){
//         console.log(number[x]);
//         x+=1;//x++; //dar daca pui x+1 ))) ceva amuzant)
//     }
// }
// checkOther(0)
// let nowWithFor = (y,numbers=[30 , 40, 20, 10, 7]) => {
//     for (; y < numbers.length; y++) {
//         console.log(numbers[y]);
//     }
// }
// nowWithFor(0)
// let nowOtherfor = (k ,numbers1=[30 , 40, 20, 10, 7]) => {
//     for (d in numbers1) {
//         if (d >= k )// sau k in numbers1 si if in scoatem
//         console.log(numbers1[d]);
//     }
// }
// nowOtherfor(0)
// const numbers1=[30 , 40, 20, 10, 7];
// for (d in numbers1) {
//     console.log(numbers1[d]);
// }
// let nowOtherfor1 = ( num ,numbers2=[30 , 40, 20, 10, 7]) => {
//     for (num of numbers2) {
//         console.log(num);
//     }
// }
// nowOtherfor1(0)
// let methodFor = (num,some=[30 , 40, 20, 10, 7] ) => {
//     some.slice(num).forEach(item => {console.log(item)
//     });
// }
// methodFor(0)
// let findFor = (num,some=[30 , 40, 20, 10, 7]) => {
//     let result = some.findLast(item => item >num);
//     console.log(result);
// }
// findFor(10)
// let findFor = (num,some=[30 , 40, 20, 10, 7]) => {
//     let result = some.find(item => item >num);
//     console.log(result);
// }
// findFor(20)
// let findFor = (num,some=[10 , 20, 30, 40, 7]) => {
//     let result = some.findIndex(item => item >= num);
//     console.log(result);
// }
// findFor()
// let findFor = (num,some=[10 , 20, 30, 40, 7]) => {
//     let result = some.findLastIndex(item => item >num);
//     console.log(result);
// }
// findFor(5)
// let mapArray = (num,some=[10 , 20, 30, 40, 7]) => {
//     let result = some.map(item => item * num);
//     console.log(result);
// }
// mapArray(1.5)
// let mapArray = (some=[10 , 20, 30, 40, 7]) => {
//     let result = some.reduce((a,b) => {
//         return a + b;
//     });
//     console.log(result)
// }
// mapArray()
//  let mapArray = (num ,some=[10 , 20, 30, 40, 7]) => {
//     let result = some.filter(item => item % num === 0);
//     console.log(result)
// }
// mapArray(4)
// const languages = ["JavaScript" ,"PHP" , "Python" , "CSS" , "HTML", "Ruby", "Java"];
// const mapArray = (arr , query) => arr.filter(element => element.toLowerCase().indexOf(query.toLowerCase()) !== -1);

// let newLanguages = mapArray(languages,"p");
// console.log(newLanguages);
// const languages = ["JavaScript", "PHP", "Python", "CSS", "HTML", "Ruby", "Java"];

// const mapArray = (arr, query) => {
//     return arr.filter(element => element.toLowerCase().indexOf(query.toLowerCase()) !== -1);
// }
// let newLanguages = mapArray(languages, "h");
// console.log(newLanguages);
//  let mapArray = (num ,some=[10 , 20, 30, 40, 7]) => {
//     let result = some.every(item => item % num === 0);
//     console.log(result)
// }
// mapArray(2)
//Home Work !!!!!!!!!!!!!!!!!!!!
// const newArray = [1, 4, 5, 1, 4, 1, 5, 5, 1, 3];
// const newEmpty = [];
// let sortArray = (arr,empty) =>{
//     for (let i=0; i < arr.length; i++){
//         for (let j = i + 1; j < arr.length; j++ ) {
//             if (arr[i] === arr[j] && !empty.includes(arr[i])){
//                 empty.push(arr[i]);{
//                 }
//             }
//         }
//     }
//     console.log(empty)
//     return empty;
// }
// sortArray(newArray,newEmpty)
// const newArray = [1, 4, 5, 1, 4, 1, 5, 5, 1, 3 ,5];

// let checkNumber = (arrData) => {
//     let sortNumber = arrData.filter((item, index) => arrData.indexOf(item) >= index);{
//         console.log(sortNumber);
//     }
//     let howMany = {};
//      arrData.forEach(item => { 
//         howMany[item] = (howMany[item] || 0) + 1;
//     });
//     console.log(howMany);
// }
// checkNumber(newArray);
// const newArray = [1, 4, 5, 1, 4, 1, 5, 5, 1, 3 ,5];

// let checkNumber = (arrData) => {
//     let maxAndmin = arrData.reduce((max,curent) => {
//         return (curent > max) ? curent : max ;
//     } , arrData[0]);

//     console.log(maxAndmin);
// }
// checkNumber(newArray);
// const newArray = [1, 4, 5, 1, 4, 1, 5, 5, 1, 3 ,5];

// let checkNumber = (arrData) => {
//     let maxAndmin = arrData.reduce((min,curent) => {
//         return (curent < min) ? curent : min ;
//     } , arrData[0]);
    
//     console.log(maxAndmin);
// }
// checkNumber(newArray);
// const newArray = [1, 4, 5, 1, 4, 1, 5, 5, 1, 3 ,5];

// let checkNumber = (findMin) => {
//     let minValue = Infinity;
//     for(item of findMin) {
//         if (item < minValue)
//             minValue = item;
//     console.log(minValue)
//     }
//     return minValue
    
// }
// checkNumber(newArray);

// const newArray = [1, 4, 5, 1, 4, 1, 5, 5, 1, 3 ,5];

// let checkNumber = (findMax) => {
//     let maxValue = -Infinity;

//     for(let item of findMax) {
//         if (item > maxValue) {
//             maxValue = item;
//         }
//     }
//     console.log(maxValue);
//     return maxValue;
// }
// checkNumber(newArray);
let index = 0;
const empty = [];
let addElement = () => {
    empty[index] = document.getElementById("add").value;
    console.log(`Element: ${empty[index]} Added at index ${index}`);
    index++;
    document.getElementById("add").value = "";
}
let displayArray = () => {
    let result = "<hr/>";
    for ( let y = 0; y < empty.length; y++){
        result += `Element ${y} = ${empty[y]} <br/>`;
    } document.getElementById("result").innerHTML = result;
}