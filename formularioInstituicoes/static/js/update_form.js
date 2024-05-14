function getValorTemaFromURL() {

    var url = window.location.href;
    var valor_tema = url.lastIndexOf("/");
    return url.substring(valor_tema + 1);
}

document.addEventListener("DOMContentLoaded", function () {
    var valor_tema = getValorTemaFromURL();

    var div_tema = document.getElementById(`temaID:${valor_tema}`).closest('div.tema')

    var div_mostrar = div_tema.querySelector('div.bloco')


    div_mostrar.style.display = 'block'

    var scrollPosition = div_tema.offsetTop - 90;

    window.scrollTo({
        top: scrollPosition,
        behavior: "smooth"
    });
});

function adicionarValorPerguntaUpdate(){
    console.log('add')
}

function removeValorPerguntaUpdate(){
    console.log('rm')
}

window.onload = function () {
    var all_perguntas = document.getElementsByClassName('multipla-resposta:True');
    var array_perguntas = Array.from(all_perguntas);

    array_perguntas.forEach(function (pergunta) {
        var resposta_dada = pergunta.querySelectorAll('div#resposta_dada');

        resposta_dada.forEach(function (resposta, index) {
            if (index === 0) {

                var botao = document.createElement("button");
                botao.type = "button";
                botao.className = "butao_adiciona";
                botao.id = "butao_adiciona";
                botao.textContent = "+";
                botao.onclick = adicionarValorPerguntaUpdate;

                resposta.appendChild(botao);
            }else{
                var botao = document.createElement("button");
                botao.type = "button";
                botao.className = "butao_remove";
                botao.id = "butao_remove";
                botao.textContent = "-";
                botao.onclick = removeValorPerguntaUpdate;

                resposta.appendChild(botao);
            }
        });
    });
};



