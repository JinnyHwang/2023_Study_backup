
/*
User의 입력값을 기억하도록 기능 추가
localStorage
개발자도구에서 Application에 들어가면
다양한 Storage를 확인할 수 있다
그 중 다루기 가장 쉬운 Local Storage를 사용

localStorage.setItem("username","jieun")
key, value 값으로 정보 저장

localStorage에 "username" key값에 value가 존재하면 Login form 없이 h1이 바로 보이도록 함
*/

const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";

function onLoginSubmit(event) {
    event.preventDefault();
    loginForm.classList.add(HIDDEN_CLASSNAME);
    //const username = loginInput.value;
    //localStorage.setItem(USERNAME_KEY, username);
    //greeting.innerText = `Hello ${username}`;
    //greeting.classList.remove(HIDDEN_CLASSNAME);
    //paintGreetings(username);
    localStorage.setItem(USERNAME_KEY, loginInput.value);
    paintGreetings();
}

function paintGreetings() {
    const username = localStorage.getItem(USERNAME_KEY);
    greeting.innerText = `Hello ${username}`;
    greeting.classList.remove(HIDDEN_CLASSNAME);
}

const saveUsername = localStorage.getItem(USERNAME_KEY);
if (saveUsername === null) {
    // show form
    loginForm.classList.remove(HIDDEN_CLASSNAME);
    loginForm.addEventListener("submit", onLoginSubmit);
} else {
    // show greeting
    //greeting.classList.remove(HIDDEN_CLASSNAME);
    //greeting.innerText = `Hello ${saveUsername}`;
    //paintGreetings(saveUsername);
    paintGreetings();
}

