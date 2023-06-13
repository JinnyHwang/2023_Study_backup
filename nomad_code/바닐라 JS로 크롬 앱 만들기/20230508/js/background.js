const images = ["0.jpeg", "1.jpeg", "2.jpeg"];

const chosenImage = images[ Math.floor( Math.random()*images.length ) ];
const bgImage = document.createElement("img");
// <img src=""/>를 만드는 것
bgImage.src = `img/${chosenImage}`;
//console.log(bgImage);
document.body.appendChild(bgImage);
// appendChild()는 body의 제일 마지막에 추가된다.
// prepend()는 body의 맨 앞에 추가됨.
// 어디에 추가되든 CSS로 조정 가능
