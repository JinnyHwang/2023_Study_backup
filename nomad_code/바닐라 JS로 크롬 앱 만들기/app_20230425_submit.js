
/*
const loginForm = document.querySelector("div#login-form");
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");
*/

/*
버튼 이벤트 바이바이
function handleBtnClick() {
    //console.dir(loginInput); // value property로 입력값을 접근가능함을 알 수 있다
    const username = loginInput.value;
    if (!username) { // username === ""
        alert("Please write your name");
    } else if (username.length > 15) { // html의 required maxlength="15"가 역할을 대신 해줌
        alert("User name is too long!");
    } else {
        console.log("hello!", username);
    }
    
}
loginButton.addEventListener("click", handleBtnClick);
*/

const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");

function onLoginSubmit(event) {
    /*
    Event.preventDefault()
    이벤트를 처리하지 않았을 때, 해당 이벤트의 기본 동작(default behavior)을 실행하지 않도록 함
    이번 예제에서는 자동으로 새로고침 하는 것을 막음
    */
    event.preventDefault();
    //console.log(event); // event 정보가 뜸
    //const username = loginInput.value;
    console.log(loginInput.value);
}

// 매개변수로 function name만 적는 이유?
// onLoginSubmit() 괄호를 덧붙이는 것은 브라우저에게 해당 func을 당장 실행하라는 뜻
// addEventListener에는 function name만 적어주고
// 지정 event가 발생했을 때만 브라우저가 해당 function을 실행시킴
// 그런데 js는 function을 실행시킬 때 첫 번때로 매개변수로 발금 발생한 event에 대한 정보를 줌
// 첫번째 매개변수로 event object를 줌
loginForm.addEventListener("submit", onLoginSubmit);

