function remover_error(){
    document.querySelector(".error-popup").remove()
}

function remover_success(){
    document.querySelector(".success-popup").remove()
}

window.onload = function (){
    const erro = document.querySelector('ul.errorlist')
    if(erro){
        erro.remove()
    }
    const username_label = document.querySelectorAll('label')[0].textContent = "Nome da Entidade:"
    console.log(username_label)
}