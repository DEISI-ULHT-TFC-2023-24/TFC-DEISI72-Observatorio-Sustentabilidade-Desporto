function remover_error(){
    document.querySelector(".error-popup").remove()
}

function remover_success(){
    document.querySelector(".success-popup").remove()
}

window.onload = function (){
    document.querySelector('ul.errorlist').remove()
}