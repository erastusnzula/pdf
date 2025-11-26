const successMessageDiv = document.getElementById("contact-message-success");
const cancelBtn = document.getElementById("contact-message-cancel");
 console.log("cancel clicked")
const disappear = ()=>{
    console.log("cancel clicked")
    cancelBtn.addEventListener('click',()=>{
        successMessageDiv.style.display = 'none';

    })
}

const timeOut = ()=>{
    successMessageDiv.style.display = 'none';

}

setTimeout(timeOut, 2000)
disappear();