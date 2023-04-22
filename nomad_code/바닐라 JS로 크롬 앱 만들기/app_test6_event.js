
const title = document.querySelector("div:nth-child(2) h1");
console.dir(title);

/*
js로 접근할 수 있는 html elements 확인 할 수 있음
onclick, ondrag, onblur.. 등 다양한 on 관련 요소
style요소
title.style.color = "blue";
*/

// event listen을 공부하자
function handleTitleClick() {
    console.log("Title was clicked!"); 
    // random data를 hex로 변환하고 올림(round)해서 string으로 변환
    title.innerText = "Title was clicked!";
    title.style.color = "#"+Math.round( Math.random()*0xffffff ).toString(16);
}

// title이 가리키고 있는 것을 클릭하면 handleTitleClick()가 실행됨
title.addEventListener("click", handleTitleClick);

/*
element 검색 방법
h1 tag의 element를 Mozilla Developer Network인 MDN에 검색
h1 html element mdn : html tag 정보 알 수 있다
그 중 web apis를 검색 :js 관점의 html Heading Element를 볼 수 있다

아니면
console.dir()로 출력해서 property를 살펴보기
그 중 앞에 on이 붙은 것이 event요소이다.
*/
function handleMouseEnter() {
    console.log("Mouse is here!");
    title.innerText = "Mouse is Enter!";
}

title.addEventListener("mouseenter", handleMouseEnter);

function handleMouseLeave() {
    console.log("Mouse is gone!");
    title.innerText = "Mouse is gone!";
}

title.addEventListener("mouseleave", handleMouseLeave);

