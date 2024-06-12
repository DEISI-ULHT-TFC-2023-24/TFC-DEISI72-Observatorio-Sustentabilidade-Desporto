function registarPopup() {
    let popup = document.getElementsByClassName('instalacaoformpopup')[0];
    popup.style.visibility = "visible"
}

function deleteButton(instalacaoID, instalacaoNome) {

    let popup = document.getElementsByClassName('eliminarinstalacaopopup')[0];

    const p = popup.querySelectorAll('div.texto_eliminar p')
    p[1].append(`(${instalacaoNome})`);
    popup.style.visibility = "visible"

    // let confirmation = confirm("Você tem certeza que deseja eliminar esta instalção?");
    // if (confirmation) {
    //     window.location.href = '/deleteinstalacao?instalacao=' + instalacaoID;
    // }

}

function esconder(){
    let popup = document.getElementsByClassName('eliminarinstalacaopopup')[0];
    popup.style.visibility = "hidden"
    const p = popup.querySelectorAll('div.texto_eliminar p')
    p[1].textContent = "Se sim, por favor, insira o nome da instalação "
    popup = document.getElementsByClassName('instalacaoformpopup')[0];
    popup.style.visibility = "hidden"

}

window.addEventListener('load', function () {
    document.getElementById("popup").addEventListener("click", function (e) {
        e = window.event || e;
        if (this === e.target) {
            let popup = document.getElementsByClassName('instalacaoformpopup')[0];
            let popupEliminar = document.getElementsByClassName('instalacaoformpopup')[0];
            popup.style.visibility = "hidden"

        }
    });
})

