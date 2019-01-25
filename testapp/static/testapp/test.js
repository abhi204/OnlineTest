let course_questions = [];
let current = 0;
let answers = []
let answer = '';
let submitResponse = null;

let progressElement = document.querySelector("#progress");
let questionElement = document.querySelector("#question");
let options = Array(document.querySelectorAll(".choice"));
let choices = document.querySelector("#choices");
let textAnswer = document.querySelector("#user-answer");
let textInputElement = document.querySelector('#text-input');

function changeAnswer(event){
    answer = event.target.value;
}

function choiceClick(event){
    answer = event.target.dataset.answer;
}

function increaseProgress(now,total){
    progressElement.innerHTML = `QUESTION(${now+1}/${total})`;
}

function hideShow(elemA, elemB){
    elemA.hidden = true;
    elemB.hidden = false;
}


function updateChoices(){
    let server_opt = ['opt_a', 'opt_b', 'opt_c', 'opt_d'];
    for (opt in server_opt){
        option = server_opt[opt];
        document.querySelector(`.${option}`).dataset.answer = course_questions[current][option];
        document.querySelector(`.${option}`).checked = false;
        document.querySelector(`#label_${option}`).innerHTML = course_questions[current][option];
    }
}

function nextQ(){
    if(!answer)
    {
        return;
    }

    answers.push(
        {
            q_id: course_questions[current].q_id,
            answer: answer
        }
    )
    current += 1;
    answer = '';
    
    if(current === course_questions.length){
        submitAnswers();
        return;
    }
    increaseProgress(current,course_questions.length);

    questionElement.innerHTML = course_questions[current].question;
    if(!course_questions[current].opt_a){
        textAnswer.value = '';
        hideShow(choices, textInputElement);
    }
    else{
        updateChoices();
        hideShow(textInputElement, choices);
    }
}



async function getQuestions(questions){
    await fetch(`/test/questions/${course_name}`)
        .then(response => response.json())
        .then(data => questions = data )
        course_questions = questions;

        // INITIAL element rendering:
        increaseProgress(current,course_questions.length);
        questionElement.innerHTML = course_questions[current].question;

        if(!course_questions[current].opt_a){
            textAnswer.value = '';
            hideShow(choices, textInputElement);
        }
        else{
            updateChoices();
            hideShow(textInputElement, choices);
        }
    };

getQuestions(course_questions);

//Submit Answers to Server
async function submitAnswers(){
    await fetch(
        `/test/${course_name}`,
        {   method: "POST",
            body: JSON.stringify(answers),
            headers: {"Content-Type": "application/json",}
        }).then(resp => resp.json())
        .then(data => submitResponse = data)
        .catch(error =>{
            window.alert("Unknown Error Occured");
            console.log(error);
        })
    if(submitResponse.response === 'success'){
        window.alert(`Your Score is:${submitResponse.score}`);
        window.location= `/test/result/${course_name}`;
    }
    else{
        window.alert(submitResponse.response);
    }
}
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    var interval = setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            submitAnswers();
            clearInterval(interval);
        }
    }, 1000);
}

window.onload = function () {
    var Minutes = 10,
    display = document.querySelector('#test_timer');
    startTimer(Minutes, display);
};


