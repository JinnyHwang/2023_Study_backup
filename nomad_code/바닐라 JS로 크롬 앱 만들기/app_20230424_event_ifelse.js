
// ctrl + shift + L : 한 번에 문자 변경하기

const h1_title = document.querySelector("div:nth-child(2) h1");
console.dir(h1_title);

// event listen을 공부하자
function handleh1_titleClick() {
    console.log("h1_title was clicked!"); 
    // random data를 hex로 변환하고 올림(round)해서 string으로 변환
    h1_title.innerText = "h1_title was clicked!";
    h1_title.style.color = "#"+Math.round( Math.random()*0xffffff ).toString(16);
}
function handleTitleClick_1() {
    if (h1_title.style.color == "blue") {
        h1_title.style.color = "tomato";
    } else {
        h1_title.style.color = "blue";
    }
}

// function에 if else문 더하기
function handleTitleClick() {
    const currColor = h1_title.style.color; // 변경 불가능
    let newColor; // 변경 가능
    if (currColor == "blue") {
        newColor = "tomato";
    } else {
        newColor = "blue";
    }
    h1_title.style.color = newColor; // 변수 값으로 element 속성 변경
    // 하지만 니꼬쌤은 js에서 html element style 변경하는 것을 좋아하지 않음
    // 언어가 섞이는걸 좋아하지 않기 때문
}

h1_title.addEventListener("click", handleTitleClick);

