

const TODOS_KEY = "todos";

const toDoForm = document.getElementById("todo-form");
const toDoInput = toDoForm.querySelector("input");
//const toDoInput2 = document.getElementById("#todo-form input");
const toDoList = document.getElementById("todo-list");

/*
todo list 저장하는 array
localstorage에는 array를 저장할 수 없음. text만 저장 가능
js object나 array나 무엇이든 string으로 바꿔주는 기능을 배울 것
JSON.stringify() : array to string
JSON.parse() : string to array
*/
//const toDos = [];
//let toDos = JSON.parse(localStorage.getItem(TODOS_KEY));
// 선언은 빈 array로
// 초기화는 아래 const savedToDos = localStorage.getItem(TODOS_KEY); code에서

/*
20230508 폴더에서는 dictionary를 원소를 갖는 array를 사용해서 삭제를 구현할 것
[{id:121212, text:"drink"}] //id는 랜덤으로, text는 localStorage에 저장된 값으로

Date.now() : msec단위로 표기해줌. 해당 값을 randomr값으로 활용할 것

*/
let toDos = []


function saveToDos() {
    //localStorage.setItem("todos", toDos); //a,b,c
    localStorage.setItem(TODOS_KEY, JSON.stringify(toDos)); //["a","b","c"]
}

/*
filter function 활용!
*/
function sexyFilter() {
    
}
// https://nomadcoders.co/javascript-for-beginners/lectures/2921

function deleteToDo(event) {
    //path 속성으로 event가 click된 위치를 할 수 있음
    //path 속성 중 target 속성으로 접근
    //해당 funtion에서는 button target으로 확인
    //target의 parentElement로 어떤 li에서 button이 호출된건지 알 수 있음
    //console.log(event.target.parentElement.innerText);
    const li = event.target.parentElement;
    const remove_id = li.id;
    li.remove();

}

function paintToDo_old(newTodo) {
    const li = document.createElement("li");

    const span = document.createElement("span");
    span.innerText = newTodo;

    const button = document.createElement("button");
    button.innerText = "❌";
    // 여기서 생성된 button들은 click event시 deleteToDo function 호출
    /* button getEventListeners() 했을 때 정보 예시
    getEventListeners(document.getElementsByTagName("button")[0])
    {click: Array(1)}
        click: Array(1)
            0: 
                listener: ƒ deleteToDo(event)
                    arguments: null
                    caller: null
                    length: 1
                    name: "deleteToDo"
                    prototype: {constructor: ƒ}
                    [[FunctionLocation]]: todo.js:24
                    [[Prototype]]: ƒ ()
                    [[Scopes]]: Scopes[2]
                    once: false
                    passive: false
                    type: "click"
                    useCapture: false
                [[Prototype]]: Object
                    constructor: ƒ Object()hasOwnProperty: ƒ hasOwnProperty()isPrototypeOf: ƒ isPrototypeOf()propertyIsEnumerable: ƒ propertyIsEnumerable()toLocaleString: ƒ toLocaleString()toString: ƒ toString()valueOf: ƒ valueOf()__defineGetter__: ƒ __defineGetter__()__defineSetter__: ƒ __defineSetter__()__lookupGetter__: ƒ __lookupGetter__()__lookupSetter__: ƒ __lookupSetter__()__proto__: (...)get __proto__: ƒ __proto__()set __proto__: ƒ __proto__()
            length: 1
            [[Prototype]]: Array(0)
                at: ƒ at()concat: ƒ concat()constructor: ƒ Array()copyWithin: ƒ copyWithin()entries: ƒ entries()every: ƒ every()fill: ƒ fill()filter: ƒ filter()find: ƒ find()findIndex: ƒ findIndex()findLast: ƒ findLast()findLastIndex: ƒ findLastIndex()flat: ƒ flat()flatMap: ƒ flatMap()forEach: ƒ forEach()includes: ƒ includes()indexOf: ƒ indexOf()join: ƒ join()keys: ƒ keys()lastIndexOf: ƒ lastIndexOf()length: 0map: ƒ map()pop: ƒ pop()push: ƒ push()reduce: ƒ reduce()reduceRight: ƒ reduceRight()reverse: ƒ reverse()shift: ƒ shift()slice: ƒ slice()some: ƒ some()sort: ƒ sort()splice: ƒ splice()toLocaleString: ƒ toLocaleString()toReversed: ƒ toReversed()toSorted: ƒ toSorted()toSpliced: ƒ toSpliced()toString: ƒ toString()unshift: ƒ unshift()values: ƒ values()with: ƒ with()Symbol(Symbol.iterator): ƒ values()Symbol(Symbol.unscopables): {at: true, copyWithin: true, entries: true, fill: true, find: true, …}
        [[Prototype]]: Object
            [[Prototype]]: Objectconstructor: ƒ Object()hasOwnProperty: ƒ hasOwnProperty()isPrototypeOf: ƒ isPrototypeOf()propertyIsEnumerable: ƒ propertyIsEnumerable()toLocaleString: ƒ toLocaleString()toString: ƒ toString()valueOf: ƒ valueOf()__defineGetter__: ƒ __defineGetter__()__defineSetter__: ƒ __defineSetter__()__lookupGetter__: ƒ __lookupGetter__()__lookupSetter__: ƒ __lookupSetter__()__proto__: (...)get __proto__: ƒ __proto__()set __proto__: ƒ __proto__()
    */
    button.addEventListener("click", deleteToDo);
    
    li.appendChild(span);
    li.appendChild(button);
    toDoList.appendChild(li);
}


function paintToDo(newTodoObj) {
    const li = document.createElement("li");
    li.id = newTodoObj.id;

    const span = document.createElement("span");
    span.innerText = newTodoObj.text;

    const button = document.createElement("button");
    button.innerText = "❌";
    button.addEventListener("click", deleteToDo);
    
    li.appendChild(span);
    li.appendChild(button);
    toDoList.appendChild(li);
}

function handleToDoSubmit(event) {
    event.preventDefault();
    const newTodo = toDoInput.value;
    toDoInput.value = "";
    //console.log(newTodo, toDoInput.value, '?');
    //페이지 새로고침하면 빈 array에 push함
    //페이지에서 새롭게 값이 입력되면 누적이 아닌 새로운 값으로 덮임
    //toDos를 localStorage에 저장된 값으로 초기화해주면 해결됨

    // 삭제 구현을 위한 array 형식 변경
    const newTodoObj = {
        text: newTodo,
        id: Date.now(),
    };
    //toDos.push(newTodo);
    toDos.push(newTodoObj);
    //paintToDo(newTodo);
    paintToDo(newTodoObj);
    saveToDos();
}

function SayHello(item) {
    console.log("Hello1 ", item);
}

// form에서 submit이 생기면 동작
toDoForm.addEventListener("submit", handleToDoSubmit);

const savedToDos = localStorage.getItem(TODOS_KEY);
if (savedToDos) {
    const parsedToDos = JSON.parse(savedToDos);
    toDos = parsedToDos;
    //forEach()는 각 원소들에 대해 function을 실행하게 함
    //parsedToDos.forEach(SayHello);
    //별도의 function을 만들지 않고 원소를 바로 사용해서 구현
    //arrow function이라고 함
    /*
    parsedToDos.forEach(element => {
            //console.log("Hello2 ", element);
    });
    */
   parsedToDos.forEach(paintToDo);
} else {
    
}
 
