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
let findFor = (num,some=[10 , 20, 30, 40, 7]) => {
    let result = some.findIndex(item => item >= num);
    console.log(result);
}
findFor(15)
// let findFor = (num,some=[10 , 20, 30, 40, 7]) => {
//     let result = some.findLastIndex(item => item >num);
//     console.log(result);
// }
// findFor(5)

