

const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");

const link = document.querySelector("a");

function onLoginSubmit(event) {
    //console.log(event);
    event.preventDefault();
    console.log(loginInput.value);
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

