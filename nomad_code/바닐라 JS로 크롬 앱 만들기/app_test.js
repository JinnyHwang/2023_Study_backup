

// console에 document입력하면 html code 보여줌
// js에 정의되어 있는 object
// console.dir(document)를 출력해보면
// document object와 관련된 정보를 볼 수 있음
// document.title를 확인하면 html에서 내가 정의한 title 정보를 볼 수 있음
//  <title>Momentum</title> 에 정의된 정보로 object가 초기화 된 것
// document.title = "New" 하면 정보를 바꿀 수 있음
// 즉, document는 js로 html 정보를 읽고, 쓸 수 있다는 것을 의미함
// js로 form을 생성하고, 사용하는 방법을 배울 것
// document 객체가 어떤 정보를 담고 있는지 호가인 필요

/*
const age = 96;
function calculateKrAge(ageOfForeigner) {
    //return ageOfForeigner + 2;
    ageOfForeigner + 2;
    return 'hi';
}

const krAge = calculateKrAge(age);
console.log(krAge);
*/
/*
const calculator = {
    plus: function (a, b) {
        return a+b;
    },
    minus: function (a, b) {
        return a-b;
    },
    times: function (a, b) {
        return a*b;
    },
    divide: function (a, b) {
        return a/b;
    },
    power: function (a, b) {
        return a**b;
    }
}

// 브라우저 console에서 변수를 입력하면 출력됨
// const로 선언한 변수를 function으로 선언하면
// function의 return type을 변수 type으로 갖는다
const pr = calculator.plus(3,5);
const mr = calculator.minus(10.1,2.5);
const tr = calculator.times(2.2,3);
const dr = calculator.divide(7,2);
const ppr = calculator.power(2,3)
*/

/*
const player = {
    name: "N",
    age: 1,
};

console.log(player);
player.name = "J";
console.log(player);
player.aaa = "wow";
console.log(player);

function plus(potato, salad){
    console.log(potato + salad);
}

plus(5, 10);
plus(1.1, 2.2);
plus(111.1, 5);
//alert("TestTest");
*/
/*
const a = 5;
let isNicoFat = true;
// var 쓰지 말기!
const toBuy = ["potato", "tomato", "pizza"];
console.log(toBuy);
toBuy.push("chicken");
console.log(toBuy);
*/

/*
2023.04.13
function sayHello(name, age){
    console.log("Hello! "+name+' your age is...'+age);
}

sayHello("jiji", 29);
sayHello("eueu", 27);

const player = {
    name: "jing",
    points: 123,
    handsome: false,
    fat: "little bit",
    sayHello: function(who){
        console.log("Hi ",who);
    },
};
player.sayHello("abc");
sayHello("umm..", 30);

// 객체 object
const playerName = "jiji";
const playerPoints = 123456;
const playerHandsome = false;
const playerFat = "little bit";
// 비효율적
//const player = [playerName, playerPoints, playerHandsome, playerFat];
const player = {
    name: playerName,
    points: playerPoints,
    handsome: playerHandsome,
    fat: playerFat
};
console.log(player);
console.log(player.fat);
player.name = "wow"; // value 변경
console.log(player);
player.description = 'test'; //key 추가
console.log(player);

// array
const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
const nonsense = [1, 2, "ttt", 33, '!!'];
//nonsense = ['new!']; // 불가능
console.log(daysOfWeek, ' ', nonsense, ' ', nonsense[nonsense.length-1]);
daysOfWeek.push("sun2");
console.log(daysOfWeek);

//const amIFat = true;
// null과 undefine 차이
const amIFat = null; //자연적으로 발생하지 않음. 값이 없음을 표시하기 위함.
let something;
console.log(amIFat);
console.log(something);
// js에서는 true, false, null
// 파이썬에서는 True, False, None으로 표기

//alert("hi");
console.log(153153); //print 역할까지 함
console.log("lululu");
console.log(1+3);
console.log(1.5*3.2);

//var a = 5, b = 3;
// js variable 선언 방법
// const : 값 변경 불가능
// let : 이후 값 초기화 가능
const a = 5, b = 2;
//let a = 5, b = 2;
//a = 3, b = 5;
const myName = "jieun";
//let myName = "jieun";

// var은 옛날 방식. 언제든 type 상관 없이 값 변동 가능
//var a = 1, b = 2, myName = "jijiji";
//myName = "jiny";
//myName = 1;
//a = 'aa';

console.log("hello! "+myName);
console.log(a+b);
console.log(a/b);
console.log(a*b);
*/
