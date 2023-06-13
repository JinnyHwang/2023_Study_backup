//function sayHello() {
//    console.log("hello");
//}

// 실행주기(msec)마다 function 호출
//setInterval(sayHello, 5000);

// 실행시간(msec)후 function 호출
//setTimeout(sayHello, 5000);

// 문자열 글자수를 항상 일정하게 가져가고 싶을 때
// padStart(), padEnd() 사용해서 문자열 앞 or 뒤를 default 문자열로 채우기
//"".padStart(2, "0");
//"".padEnd(2, "-");

const clock = document.querySelector("h2#clock");

function  getClock() {
    const date = new Date();
    const hours = String(date.getHours()).padStart(2,"0");
    const minutes = String(date.getMinutes()).padStart(2,"0");
    const seconds = String(date.getSeconds()).padStart(2,"0");
    //console.log(`${date.getHours()}:${date.getUTCMinutes()}:${date.getSeconds()}`);
    //clock.innerText = `${date.getHours()}:${date.getUTCMinutes()}:${date.getSeconds()}`;
    clock.innerText = `${hours}:${minutes}:${seconds}`;
}
setTimeout(getClock, 10);
setInterval(getClock, 1000);


