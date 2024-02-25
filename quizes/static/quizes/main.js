const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalbody=document.getElementById('modal-body-confirm')
const startBtn =document.getElementById("start-button")
const url = window.location.href
modalBtns.forEach(modalBtn=>modalBtn.addEventListener('click',()=>{
    const pk =modalBtn.getAttribute("data-pk")
    const category =modalBtn.getAttribute("data-quiz")
    const numberOfquestions =modalBtn.getAttribute("data-questions")
    const time = modalBtn.getAttribute("data-time")
    const pass =modalBtn.getAttribute("data-pass")


    modalbody.innerHTML=`
       <div class = "text-muted">
          <ul>
              <li>number of questions : <b>${ numberOfquestions}</b></li>

              <li>score to pass : <b>${pass}%</b></li>

              <li>time : <b>${time} min</b></li>

          </ul>
       </div>
    `
    startBtn.addEventListener("click",()=>{
        window.location.href = url+pk
    })
}))