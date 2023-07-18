
// localStorage에서 사용할 key 값
const USERNAME_KEY = "username";
const CLASS_HIDDEN = "hidden"; //CSS에 정의되어 있는 hidden class name

// 사용할 login 관련 객체 선언
const loginForm = document.querySelector("#login-form"); // # id값으로 접근
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("h1#greeting");

// localStorage에서 USERNAME_KEY값으로 저장된 data를 가져옴
const saveUsername = localStorage.getItem(USERNAME_KEY);

// USERNAME_KEY key값으로 저장된 data가 없으면 form display, submit 기능 추가
if (saveUsername === null) {
    loginForm.classList.remove(CLASS_HIDDEN); // 숨김 해제
    loginForm.addEventListener("submit", onLoginSubmit);
} else { // USERNAME_KEY key값 data 존재하면 h1 display
    paintGreetings();
}

function onLoginSubmit(event) {
    // "submit"으로 진행되는 기본 event 사용 안함
    event.preventDefault();
    localStorage.setItem(USERNAME_KEY, loginInput.value);
    paintGreetings();
    loginForm.classList.add(CLASS_HIDDEN);
}

function paintGreetings() {
    const username = localStorage.getItem(USERNAME_KEY);
    greeting.innerText = `Hello ${username}`; //'아님 `임
    greeting.classList.remove(CLASS_HIDDEN); // 숨김 해제
}

