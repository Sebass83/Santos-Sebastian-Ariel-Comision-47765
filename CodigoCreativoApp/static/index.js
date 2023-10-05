const menu = document.querySelector('.material-symbols-outlined')
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