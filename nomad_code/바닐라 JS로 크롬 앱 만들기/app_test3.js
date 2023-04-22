// 브라우저에서 사용할 수 있는 document object

// id로 element를 가져올 수 있음
const title = document.getElementById("title");
//console.log(title);
/*
js에서 html 읽기 다양한 정보를 출력해줌
id: "title"
inert: false
innerHTML: "Grab me!"
innerText: "Grab me!"
*/
console.dir(title); 
title.innerText = "Got you!";
/*
html 
before: <h1 id="title">Grab me!</h1>
after: <h1 id="title">Got you!</h1>
js에서 html id값으로 element를 가져와서 값을 변경 가능
js관점에서의 html을 보여줌
html에서 항목을 가져와서 js에서 항목들 변경
*/

console.log(title.id);
console.log(title.className);


