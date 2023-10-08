const menu = document.querySelector('.material-symbols-outlined')
const message = document.querySelector('.error-message')

if(message){
    setTimeout(() =>{
        message.remove();
    },'2900')

}

const ul = document.querySelector('nav ul')
menu.addEventListener('click', (e) => {
    if (e.target.innerHTML == "close"){
        e.target.innerHTML = "menu"
        ul.classList.remove("visible")
    }else{
        e.target.innerHTML="close"
        ul.classList.add("visible")
    }
})

if(document.URL.includes("/auth/logout/")){
    setTimeout(() =>{
        window.location.replace(document.location.origin);
    },'3000')
}
