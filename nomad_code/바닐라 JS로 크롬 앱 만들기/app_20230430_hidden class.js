

const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const link = document.querySelector("a");

const HIDDEN_CLASSNAME = "hidden";

// input 입력창을 없애고 h1(기본 hidden)에 입력값 표시
function onLoginSubmit(event) {
    //console.log(event);
    event.preventDefault(); //submit 할 때 기본 동작 막음
    //console.log(loginInput.value);
    //const username = loginInput.value;
    loginForm.classList.add(HIDDEN_CLASSNAME); //CSS에서 정의한 hidden class를 적용
    //console.log(username);
    const username = loginInput.value;

    //greeting.innerText = "Hello " + username;
    greeting.innerText = `Hello ${username}`; //백틱기호
    greeting.classList.remove(HIDDEN_CLASSNAME);
}

function handleLinkClick(event) {
    // PointerEvent : https://javascript.info/pointer-events 전자기기 다양성으로 MouseEvent가 아닌 PointerEvent 사용
    //console.log(event);
    event.preventDefault();
    console.dir(event); // defaultPrevented: true 뜸
    //alert("click!"); // alert 동작이 완료되면 default 동작이 실행됨
}

loginForm.addEventListener("submit", onLoginSubmit);
link.addEventListener("click", handleLinkClick)

