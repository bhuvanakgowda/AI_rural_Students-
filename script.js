function welcome(){

alert("Welcome to EduAssist AI!");

}

console.log("EduAssist AI Loaded");
async function sendQuestion(){

let question=document.getElementById("question").value;

let form=new FormData();

form.append("question",question);

let response=await fetch("/ask",{

method:"POST",

body:form

});

let data=await response.json();

document.getElementById("chatBox").innerHTML+=`

<p>

<b>You:</b> ${question}

</p>

<p>

<b>EduAssist AI:</b>

${data.answer}

</p>

<hr>

`;

document.getElementById("question").value="";

}
async function loadQuiz(){

let res=await fetch("/quizdata");

let data=await res.json();

let html="";

data.questions.forEach((q,i)=>{

html+=`<h3>${i+1}. ${q.question}</h3>`;

q.options.forEach(option=>{

html+=`

<input type="radio"

name="q${i}">

${option}

<br>

`;

});

});

document.getElementById("quiz").innerHTML=html;

}
