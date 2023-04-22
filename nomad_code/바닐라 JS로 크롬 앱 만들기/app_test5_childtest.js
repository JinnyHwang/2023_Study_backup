/*
[html code]
   <h1 class="test1" id="title">no div no class</h1>

    <div class="hello" id="helloid">
        <h1>Grab me!</h1>
        <h1>Wow!</h1>
    </div>
    <div class="hello">
        <h1>Grab me2!</h1>
    </div>
    <div class="hello" id="helloid2">
        <h1>Grab me3!</h1>
    </div>
    
    <h1 class="test2" id="helloid">test id</h1>

*/

/*
html에서 js를 load하기 때문에 js에서 document object를 통해 html에 접근할 수 있음
<script src="app.js"></script>

*/
//console.dir(document);

const title = document.querySelector("#helloid2");
console.log(title);

/*
first-child
nth-child(n)
last-child
html내부에서 child가 어떤 것을 가르키고 있는 것인지 공부 필요
*/

//const title2 = document.querySelector(".hello:first-child h1");
//const title2 = document.querySelectorAll("#helloid2.hello");
//const title2 = document.querySelector("div.hello:first-child");
//const title2 = document.querySelector(".hello:first-child"); // null. html code에서 hello class가 맨 처음 선언되어 있지 않기 때문에 null
//const title2 = document.querySelector(".hello:nth-child(2) h1");
//const title2 = document.querySelector(".test1:first-child"); // <h1 class="test1" id="title">no div no class</h1>
//title2.innerText = "Change Test?";
//const title2 = document.querySelector("div:nth-child(2)");
/*
    <div class="hello" id="helloid">
        <h1>Grab me!</h1>
        <h1>Wow!</h1>
    </div>
*/
const title2 = document.querySelector("div:nth-child(2) h1");
console.log(title2);
title2.innerText = "nth-child(2)";

const title3 = document.querySelector(".hello:nth-child(3) h1");
//const title3 = document.querySelector("h1.hello:last-child"); // <h1>Wow!</h1>
console.log(title3);
 