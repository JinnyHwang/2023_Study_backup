
// ctrl + shift + L : 한 번에 문자 변경하기

const h1_title = document.querySelector("div:nth-child(2) h1");
console.dir(h1_title);

/*
js로 접근할 수 있는 html elements 확인 할 수 있음
onclick, ondrag, onblur.. 등 다양한 on 관련 요소
style요소
h1_title.style.color = "blue";
*/

/*
element 검색 방법
h1 tag의 element를 Mozilla Developer Network인 MDN에 검색
h1 html element mdn : html tag 정보 알 수 있다
그 중 web apis를 검색 :js 관점의 html Heading Element를 볼 수 있다

아니면
console.dir()로 출력해서 property를 살펴보기
그 중 앞에 on이 붙은 것이 event요소이다.
*/

// event listen을 공부하자
function handleh1_titleClick() {
    console.log("h1_title was clicked!"); 
    // random data를 hex로 변환하고 올림(round)해서 string으로 변환
    h1_title.innerText = "h1_title was clicked!";
    h1_title.style.color = "#"+Math.round( Math.random()*0xffffff ).toString(16);
}
function handleMouseEnter() {
    console.log("Mouse is here!");
    h1_title.innerText = "Mouse is Enter!";
}
function handleMouseLeave() {
    console.log("Mouse is gone!");
    h1_title.innerText = "Mouse is gone!";
}
// window resize event
function handleWindowResize() {
    document.body.style.backgroundColor = "tomato";
}
//copy event
function handleWindowCopy() {
    alert("copier!");
}
// 브라우저가 wifi에 연결되어 있는지, 아닌지 알 수 있는 이벤트
function handleWindowOffline() {
    alert("WIFI is disconnect!");
}
function handleWindowOnline() {
    alert("WIFI is GOOD!");
}
// h1_title이 가리키고 있는 것을 클릭하면 handleh1_titleClick()가 실행됨
/*
h1_title.addEventListener("click", handleh1_titleClick);
h1_title.onclick = handleh1_titleClick;
두 가지 방식 중 어떤 방식을 더 쓰는게 좋을까?
addEventListener() 추천
.removeEventListener()로 이벤트를 지울 수도 있음
*/
h1_title.addEventListener("click", handleh1_titleClick);
//h1_title.onclick = handleh1_titleClick; // 위와 동일한 표현
h1_title.addEventListener("mouseenter", handleMouseEnter);
h1_title.addEventListener("mouseleave", handleMouseLeave);

window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);
window.addEventListener("offline", handleWindowOffline);
window.addEventListener("online", handleWindowOnline);

