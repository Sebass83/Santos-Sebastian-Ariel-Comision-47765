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
    if (h1) {

        if (h1.innerHTML === 'Te has deslogueado...') {
            setTimeout(() => {
                window.location.replace(document.location.origin);
            }, '3000')
        }
    }
}

if (document.URL.includes("/mis-post/")) {
    const cancelarBtns = document.querySelectorAll('.secondary')
    if (cancelarBtns.length > 0) {
        cancelarBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                postId = parseInt(btn.dataset.data)
                ruta = `/eliminar-post/${postId}`
                let opcion = confirm(`Estas seguro de querer eliminar el post con ID: ${postId}`)
                if (opcion) {
                    window.location.replace(document.location.origin + ruta)
                }

            })

        });
    }

}

if (document.URL.includes("/mis-mensajes/")) {
    const verBtns = document.querySelectorAll('.primary');

    if (verBtns.length > 0) {
        verBtns.forEach(btn => {
            btn.addEventListener("click", (e) => {
                e.preventDefault()
                if (btn.innerHTML === "Leer") { 
                temp = btn.parentNode
                mensajes = temp.parentNode.children[2]

                if (mensajes.classList.length == 2) {
                    mensajes.classList.remove("mostrar")
                    console.log(mensajes.classList)
                } else {
                    mensajes.classList.add("mostrar")
                    console.log(mensajes.classList)
                }}
            })
        })
    }

}



