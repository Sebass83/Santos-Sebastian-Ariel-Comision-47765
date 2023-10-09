const menu = document.querySelector('.material-symbols-outlined')
const message = document.querySelector('.error-message')

if (message) {
    setTimeout(() => {
        message.remove();
    }, '2900')

}

const ul = document.querySelector('nav ul')
menu.addEventListener('click', (e) => {
    if (e.target.innerHTML == "close") {
        e.target.innerHTML = "menu"
        ul.classList.remove("visible")
    } else {
        e.target.innerHTML = "close"
        ul.classList.add("visible")
    }
})

if (document.URL.includes("/auth/logout/")) {
    setTimeout(() => {
        window.location.replace(document.location.origin);
    }, '3000')
}

if (document.URL.includes("/auth/editarPerfil/")) {
    const h1 = document.querySelector('.container-form h1')
    if(h1){
  
    if (h1.innerHTML === 'Te has deslogueado...') {
        setTimeout(() => {
            window.location.replace(document.location.origin);
        }, '3000')
    }
}
}


