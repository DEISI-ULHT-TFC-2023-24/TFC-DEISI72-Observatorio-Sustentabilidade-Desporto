function registarPopup() {
    let popup = document.getElementsByClassName('instalacaoformpopup')[0];
    popup.style.visibility = "visible"
}


function deleteButton(instalacaoID, instalacaoNome) {
    let popup = document.getElementsByClassName('eliminarinstalacaopopup')[0];

    const p = popup.querySelectorAll('div.texto_eliminar p');
    p[1].textContent = "Se sim, por favor, insira o nome da instalação " + `(${instalacaoNome})`;
    popup.style.visibility = "visible";

    const deletebutton = popup.querySelectorAll("div.butoes_popup button")[1];

    if (deletebutton._handleClick) {
        deletebutton.removeEventListener('click', deletebutton._handleClick);
    }

    function handleClick() {
        const inputBox = popup.querySelector('input');

        // Remove qualquer parágrafo de erro existente
        const existingErrorP = inputBox.nextElementSibling;
        if (existingErrorP && existingErrorP.classList.contains('error')) {
            existingErrorP.remove();
        }

        if (inputBox.value === instalacaoNome) {
            window.location.href = '/deleteinstalacao?instalacao=' + instalacaoID;
        } else {
            inputBox.style.border = "2px solid red";
            const errorP = document.createElement('p');
            errorP.className = 'error';
            errorP.textContent = 'Os nomes não coincidem';
            errorP.style.color = 'red';
            inputBox.insertAdjacentElement('afterend', errorP);
        }
    }

    deletebutton.addEventListener('click', handleClick);

    deletebutton._handleClick = handleClick;
}


function esconder() {
    let popup = document.getElementsByClassName('eliminarinstalacaopopup')[0];
    popup.style.visibility = "hidden"

    const deletebutton = popup.querySelectorAll("div.butoes_popup button")[1];

    if (deletebutton._handleClick) {
        deletebutton.removeEventListener('click', deletebutton._handleClick);
        deletebutton._handleClick = null;
    }

    const inputBox = popup.querySelector('input')
    inputBox.style.border = "2px solid rgba(0, 0, 0, 0.32)"
    inputBox.value = ""
    const error = popup.querySelector('p.error')

    if (error) {
        error.remove()
    }


    const p = popup.querySelector('div.texto_eliminar p.txt')
    p.textContent = "Se sim, por favor, insira o nome da instalação "
    popup = document.getElementsByClassName('instalacaoformpopup')[0];
    popup.style.visibility = "hidden"


}

window.addEventListener('load', function () {
    document.getElementById("popup").addEventListener("click", function (e) {
        e = window.event || e;
        if (this === e.target) {
            let popup = document.getElementsByClassName('instalacaoformpopup')[0];
            popup.style.visibility = "hidden"

        }
    });
})

