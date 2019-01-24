let course_questions = [];
let current = 0;
let answers = []
let answer = '';

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
        console.log(answers)
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