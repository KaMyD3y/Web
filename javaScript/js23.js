let check = (i,lab=[30 , 40, 20, 10, 5]) => {
    do { console.log (lab[i]); 
        i++;
    } while (i < lab.length);
}
check(0)
let checkOther = (x,number=[30 , 40, 20, 10, 5]) => {
    while (x < number.length){
        console.log(number[x]);
        x+=1;//x++; //dar daca pui x+1 ))) ceva amuzant)
    }
}
checkOther(0)
// let nowWithFor = (y,numbers=[30 , 40, 20, 10, 7]) => {
//     for (; y < numbers.length; y++) {
//         console.log(numbers[y]);
//     }
// }
// nowWithFor(0)
let nowOtherfor = (k ,numbers1=[30 , 40, 20, 10, 7]) => {
    for (d in numbers1) {
        if (d >= k )
        console.log(numbers1[d]);
    }
}
nowOtherfor(0)
// const numbers1=[30 , 40, 20, 10, 7];
// for (d in numbers1) {
//     console.log(numbers1[d]);
// }