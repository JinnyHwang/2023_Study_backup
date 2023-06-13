const quotes = [
    {
        quote: "Be yourself; everyone else is already taken.",
        author: "Oscar Wilde",
    },
    {
        quote: "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
        author: "Albert Einstein",
    },
    {
        quote: "So many books, so little time.",
        author: "Frank Zappa",
    },
    {
        quote: "You only live once, but if you do it right, once is enough.",
        author: "Mae West",
    },
    {
        quote: "If you tell the truth, you don't have to remember anything.",
        author: "Mark Twain",
    },
    {
        quote: "A friend is someone who knows all about you and still loves you.",
        author: "Elbert Hubbard",
    },
    {
        quote: "'Classic' - a book which people praise and don't read.",
        author: "Mark Twain",
    },
    {
        quote: "I love mankind ... it's people I can't stand!!",
        author: "Charles M. Schulz",
    },
    {
        quote: "Knowing yourself is the beginning of all wisdom.",
        author: "Aristotle",
    },
    {
        quote: "The only true wisdom is in knowing you know nothing.",
        author: "Socrates",
    },
    ];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");
//console.log(quote);
//console.log(author);

/*
Math.random() // 0~1 사이의 숫자 제공
Math.round() // 소숫점 반올림해서 정수형으로
Math.ceil() // 소숫점 올림해서 정수형으로
Math.floor() // 소숫점 내림해서 정수형으로
*/

//console.log( quotes[Math.floor(Math.random()*quotes.length)]);
const todaysQuote = quotes[Math.floor(Math.random()*quotes.length)];
quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;

