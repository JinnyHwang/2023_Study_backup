
// ctrl + shift + L : 한 번에 문자 변경하기
//const h1_title = document.querySelector("div:first-child h1");
const h1_title = document.querySelector("div.hello:first-child h1");
//const h1_title = document.querySelector(".hello h1");

/*
style 정의는 js가 아니고 css에서 처리
js에서는 css에서 정의한 active class를 h1_title에 적용하는 것
javascrip가 css에 직접 대화하지 않음
js는 html을 변경
css는 html을 바라보고있음
*/
function handleTitleClick_1() {
    // .className은 getter면서 setter임
    //h1_title.className = "active";
    // class name을 정의하지 않아서 브라우저 클릭시 log 내용이 뜨지 않음
    // 브라우저 실행 중 해당 tag의 class name을 설정하면 log에 남음
    //console.log(h1_title.className);

    // 그런데 class name을 하나하나 raw string으로 설정해서 code를 세우면 오타 위험이 있음
    // 변수 활용을 생활화하자
    const clickedClass = "clicked"

    if (h1_title.className === clickedClass) {
        h1_title.className = ""; // className을 비워줌
    } else {
        h1_title.className = clickedClass;
    }
}

/*
class name을 바꾸는 다른 방법은? classList 사용
classList는 class들의 목록으로 작업할 수 있게 함
className은 이전 class를 신경쓰지 않고 모두 교체함
classList에는 다양한 function들이 있음
mdn wed docs에서 DOMTokenList를 검색
DOMTokenList.contains()은 명시한 class가 HTML element의 class에 포함되어 있는지 말해줌
태그 하나에 class를 여러개 포함할 수 있음
remove() class 제거 / add() class 추가

기존 값은 유지하면서 새로운 class 추가, 제거
그리고 html에서 맨 처음 정의한 font 클래스 정보가 남아있기 때문에
클릭해도 font 정보 남아있음
*/
function handleTitleClick_2() {

    const clickedClass = "clicked"
    // class list가 clicked를 포함하고 있는지만 확인
    if (h1_title.classList.contains(clickedClass)) {
        h1_title.classList.remove(clickedClass); // className을 비워줌
    } else {
        h1_title.classList.add(clickedClass);
    }
}

/*
DOMTokenList.toggle()
class name이 존재하는지 우선 확인함
class name이 존재하지 않으면 추가, 존재하면 삭제
위에 구현한 handleTitleClick_2() 역할이 똑같음
*/
function handleTitleClick() {
    //const clickedClass = "clicked"
    h1_title.classList.toggle("clicked");
}

h1_title.addEventListener("click", handleTitleClick);
