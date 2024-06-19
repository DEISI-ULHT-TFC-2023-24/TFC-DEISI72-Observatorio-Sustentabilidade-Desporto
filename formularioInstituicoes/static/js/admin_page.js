function send_dashboard(id_instalacao) {
    window.location.href = `/dashboard_energia_staff?instalacao=${id_instalacao}`;
}

function mostrarPopup() {
    let popup = document.getElementsByClassName('adicionaravaliacaopopup')[0];
    popup.style.visibility = "visible"
}

function esconder_confirmacao() {
    let popup = document.getElementsByClassName('confirmapopup')[0];
    popup.style.visibility = "hidden"

}

function esconder_inicial() {
    let popup = document.getElementsByClassName('adicionaravaliacaopopup')[0];
    popup.style.visibility = "hidden"

}

function esconder_inicial_mostra_confirmacao() {
    let popup_inicial = document.getElementsByClassName('adicionaravaliacaopopup')[0];
    popup_inicial.style.visibility = "hidden"

    let popup_confirmar = document.getElementsByClassName('confirmapopup')[0];
    popup_confirmar.style.visibility = "visible"
}

window.onload = function () {
    const date = new Date().getFullYear()
    document.getElementById('currentYear').textContent = `O ano que irá ser registado nesta avaliação é  ${date}`;
}

