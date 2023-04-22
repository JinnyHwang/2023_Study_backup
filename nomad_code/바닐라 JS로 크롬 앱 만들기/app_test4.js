// html에서 항목을 가져올 때 id보다 className을 주로 사용한다

/*
const title = document.getElementById("title");
title.innerText = "Test";
console.log(title.className);

<h1 class="hello" id="title">Test</h1>
<h1 class="hello" id="title">Grab me!</h1>
<h1 class="hello" id="title">Grab me!</h1>
<h1 class="hello" id="title">Grab me!</h1>
<h1 class="hello" id="title">Grab me!</h1>

같은 id값을 가진 항목이 여러개이면 하나면 변경함
id가 없으면 error 발생
Uncaught TypeError: Cannot set properties of null (setting 'innerText')
*/

/*
[html code]
    <h1 class="hello">Grab me!</h1>
    <h1 class="hello">Grab me!</h1>
    <h1 class="hello">Grab me!</h1>
    <h1 class="hello">Grab me!</h1>
    <h1 class="hello">Grab me!</h1>

const hellos = document.getElementsByClassName("hello");
console.log(hellos);

HTMLCollection(5) [h1.hello, h1.hello, h1.hello, h1.hello, h1.hello]
0: h1.hello
1: h1.hello
2: h1.hello
3: h1.hello
4: h1.hello
length: 5
[[Prototype]]: HTMLCollection

같은 class name을 가진 모든 항목들에 접근 할 수 있다
*/

/*
tag name으로 element들을 가져올 수 있음
tag : anchor, div, section, button 등을 의미함
*/

// h1 태그를 가진 모든 항목들이 title에 arr 형태로 저장됨
/*
[html code]
    <h1 id="title">no div no class</h1>
    
    <div class="hello">
        <h1>Grab me!</h1>
        <h1>Wow!</h1>
    </div>

const title = document.getElementsByTagName("h1");
console.log(title);

app.js:54 <h1>​Grab me!​</h1>​


const title2 = document.querySelector(".hello h1");
console.log(title2);

<h1>Grab me!</h1>
*/

const title = document.getElementsByTagName("h1");
console.log(title);

/*
element를 가져오는 방식
CSS selector를 사용해서 검색할 수 있음
element를 CSS 방식으로 검색할 수 있음 ".hello h1"
hello class에서 h1을 가져와라

querySelector() : Returns the first element that is a descendant of node that matches selectors.
hello class가 여러개있어도 맨 처음 항목만 가져온다
*/
//const title2 = document.querySelector("div h1");
const title2 = document.querySelector(".hello h1");
//const title2 = document.querySelector(".hello h1:first-child");
console.log(title2);

/*
[html code]
    <h1 id="title">no div no class</h1>
    <div class="hello">
        <h1>Grab me!</h1>
        <h1>Wow!</h1>
    </div>
    <div class="hello">
        <h1>Grab me2!</h1>
    </div>
    <div class="hello">
        <h1>Grab me3!</h1>
    </div>

    
const title = document.getElementsByTagName("h1");
console.log(title);

HTMLCollection(5) [h1#title, h1, h1, h1, h1, title: h1#title]


const title3 = document.querySelectorAll(".hello h1");
console.log(title3)

NodeList(4) [h1, h1, h1, h1]


const title3 = document.querySelectorAll(".hello h1:first-child");
console.log(title3);

NodeList(3) [h1, h1, h1]

*/

/*
조건에 부합하는 모든 항목을 arr 형식으로 가져온다
querySelectorAll() : Returns all element descendants of node that match selectors.
*/
//const title3 = document.querySelectorAll(".hello h1");
const title3 = document.querySelectorAll(".hello h1:first-child");
console.log(title3);
title3[1].innerText = "inner test test";


/*
getElementById()가 아닌
querySelector()를 사용해서 id로 접근하는 방식
id를 의미하는 "#"를 사용
querySelector에서는 CSS selector 자체를 전달한다
"#hello h1"
"#hello form"
이러한 방식으로 querySelector()는 getElementById()보다 활용도가 높다
*/
const title4 = document.querySelector("#helloid");
console.log(title4);
/*
    <div class="hello" id="helloid">
        <h1>Grab me!</h1>
        <h1>Wow!</h1>
    </div>
*/

const title5 = document.querySelector("#helloid h1");
console.log(title5);
// <h1>Grab me!</h1>
title5.innerText = "inner text test22";

const title6 = document.querySelectorAll("#helloid");
console.log(title6);
title6[title6.length] = "last text test";
// NodeList(2) [div#helloid.hello, div#helloid.hello]
// NodeList(3) [div#helloid.hello, div#helloid.hello, h1#helloid] // <h1 id="helloid">test id</h1> 추가


/*
[html code]
    <div class="hello">
        <h1>Grab me!</h1>
    </div>


*/

