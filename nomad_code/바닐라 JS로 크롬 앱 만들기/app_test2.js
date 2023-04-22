

/*
js
== : equal operator : 값만 같으면 true
=== : strict equal operator : 값과 data type이 모두 동일해야 true
*/
const a = "15";

// js에서는 int, float 구분 없이 number
// 일반적인 숫자 외에 Infinity, -Infinity, Nan 같은 특수 값도 숫자형에 포함되어 있음
const b = 15;
const c = 15.0;

const a2 = b.toString(); //toString(15) 이렇게 쓰면 안됨! undefine뜸
console.log(a, a2, typeof a2, a== a2); // 15 15 string true

console.log(typeof a, typeof b, typeof c); // string number number
console.log(a == b, b == c); // true true
console.log(a === b, b === c); // false true

const age = parseInt(prompt("test"));

if (isNaN(age)) {
    console.log("input data is not number");
} else {
    console.log(age, typeof age);
    if (age < 0) {
        console.log("Please input positive number");
    } else if (age<18) {
        console.log("You are too young");
    } else if (age>80) {
        console.log("You can do everything");
    } else if (age>50) {
        console.log("Please Stop Drink for you");
    } else {
        console.log("You can drink");
    }
}

/*
const age = parseInt(prompt("Test"));
console.log(age);
// int로 형변환이 불가능 한 경우
// return NaN : not a number
// data or NaN return 값 대신 boolean을 원하면
// isNaN() 사용
console.log(isNaN(age));

// 오래된 방식
let age = prompt("How old ar you?");
console.log(typeof age, isNaN(age)); //당연 string

// 형변환은?
age = parseInt(age);
console.log(typeof age, isNaN(age)); // number

const age2 = parseInt(prompt("Tell me your age!"));
console.log(age2, typeof age2); // 12 'number'

console.log(isNaN(age2));
// number type인가? return boolean형
console.log(isNaN(age), isNaN(age2));

// NaN? Not a Number
// 숫자가 아니면 true / 숫자 or 숫자로 변환될 수 있으면 false
*/
