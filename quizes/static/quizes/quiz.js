const url=window.location.href
const quizBox=document.getElementById("quiz-box")


const activateTimer=(time)=>{
    if(time.toString().length<2){
        timerBox.innerHTML=`<b>0${time}:00</b>`
    }

    else{
        timerBox.innerHTML=`<b>0${time}:00</b>`
    }

    let minutes=time-1
    let seconds=60
    let displaySecond
    let displayMinutes


    const timer=setInterval(()=>{
           seconds --
           if(seconds<0){
            seconds=59
            minutes --
           }

           if(minutes.toString().length<2){
            displayMinutes="0"+minutes
           }

           else{
            displayMinutes=minutes
           }


           if(seconds.toString().length<2){
            displaySecond="0"+seconds
           }

           else{
            displaySecond=seconds
           }

           if(minutes===0 &&seconds===0){
            timerBox.innerHTML="<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert("Time Over")
                sendData()
            },500)
           }
           timerBox.innerHTML=`<b>${displayMinutes}:${displaySecond}</b>`
           
    },1000)


}

$.ajax({
    type:"GET",
    url:`${url}data`,
    success:function(response){
        // console.log(response);
        data=response.data
        data.forEach(el => {
            for (const [question,answers] of Object.entries(el)){
               quizBox.innerHTML+=`
               <hr>
               <div class="mb-5 qst_container">
               <b>${question}</b>
           
               </div>
               `

               answers.forEach(answer=>{
                quizBox.innerHTML+=`
                <div class="ans_container">
                  <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                  <label for="${question}">${answer}</label>
                </div>
                `
               })
            }
        });
        activateTimer(response.time)
    },
})

const quizForm=document.getElementById("quiz-form")
const csrf=document.getElementsByName("csrfmiddlewaretoken")
const submitBtn=document.getElementById("submit_btn")
console.log(submitBtn);



const sendData=()=>{
   const elements=[...document.getElementsByClassName("ans")]
   const data={}
   data['csrfmiddlewaretoken']=csrf[0].value
   elements.forEach(el=>{
    if(el.checked){
        data[el.name]=el.value
    }

    else{
        if(!data[el.name]){
            data[el.name]=null
        }
    }
   })
   const scoreBox=document.getElementById("score-box")
   const resultBox=document.getElementById("result-box")




   $.ajax({
    
    type:"POST",
    url:`${url}save/`,
    data:data,
    success:function(response){
        const results=response.result
        const x=document.getElementById("quiz-form").style.display="none";
        scoreBox.innerHTML=`${response.passed ? "CONGRATILATIONS !!! " : "Upssss.....!!!! You Are Fail"} Your Score is ${response.score}`


        results.forEach(res=>{
            const resDiv=document.createElement("div")
            for(const[question,resp] of Object.entries(res)){
                  resDiv.innerHTML+=question
                  const cls=['container','p-3','text-light','h3']
                  resDiv.classList.add(...cls)

                  if(resp=="not answered"){
                    resDiv.innerHTML+='- Not Answered'
                    resDiv.classList.add("bg-warning")
                  }

                  else{
                    const answer=resp["answered"]
                    const correct=resp["correct_answer"]
                    if (answer==correct){
                        resDiv.classList.add("bg-success")
                        resDiv.innerHTML+=` answered:${answer}`
                        resDiv.innerHTML+=` | status:Right`
                    }

                    else{
                        resDiv.classList.add("bg-danger")
                        resDiv.innerHTML+=` | correct:${correct}`
                        resDiv.innerHTML+=` | answered:${answer}`
                        resDiv.innerHTML+=` | status:Wrong`
                    }
                  }
            }
            resultBox.append(resDiv)
        })
    },
    error:function(error){
        console.log(error);
    }
   })
}

quizForm.addEventListener('submit',e=>{
    e.preventDefault()
    sendData()
})


const submitBtnTimer=document.getElementById("submit_btn")
console.log("Submit Btn: "+submitBtnTimer);
function StopCount(){
    console.log("Stop Timer");
}
console.log("Timer "+timer);