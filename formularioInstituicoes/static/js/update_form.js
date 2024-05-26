function getValorTemaFromURL() {

    var url = window.location.href;
    var valor_tema = url.lastIndexOf("/");
    return url.substring(valor_tema + 1).split('?')[0];
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
    var div_copiar = this.closest("div#resposta_dada");

    var div_adicionar = div_copiar.closest('div#boxResposta').querySelector('div')

    var div_copidado = div_copiar.cloneNode(true)
    var limpar_texto = div_copidado.querySelector('span > div > input')
    limpar_texto.value = ""

    div_copidado.querySelector("button").remove()

    var botaoRemover = document.createElement('button');
    botaoRemover.type = 'button';
    botaoRemover.className = 'butao_remove';
    botaoRemover.innerText = '-';
    botaoRemover.onclick = removeValorPerguntaUpdate

    div_copidado.appendChild(botaoRemover)
    div_adicionar.appendChild(div_copidado)
}

function removeValorPerguntaUpdate(){
    var div_eliminar = this.closest("div#resposta_dada");
    div_eliminar.remove()
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

function limpar_valores_form() {

    var confirmation = window.confirm("Têm a certeza que deseja limpar o formulário?");

    // If OK is clicked, perform the action
    if (confirmation) {
        var div_tema = event.target.closest('div').closest('form');

        var allSubtemas = div_tema.querySelectorAll('div.bloco_subtema')

        var elementosVisiveis = Array.from(allSubtemas).filter(function (elemento) {
            var display = window.getComputedStyle(elemento).getPropertyValue('display');
            return display !== 'none';
        });

        elementosVisiveis.forEach(function (elemento) {

            var alltr = elemento.querySelectorAll('tr')
            alltr.forEach(function (tr) {
                var string = 'multipla-resposta:True'
                var respostas_multiplas = Array.from(tr.getElementsByClassName(string))


                respostas_multiplas.forEach(function (respostas){
                    respostas.querySelectorAll('div#resposta_dada').forEach(function (resposta, index){
                        if(index !== 0){
                            resposta.remove()
                        }
                    })
                })

                var allrespostas = tr.querySelectorAll('div#resposta_dada')

                allrespostas.forEach(function (resposta) {

                    var allinputs = resposta.querySelectorAll('input')
                    allinputs.forEach(function (input) {

                        if (input.type === 'number' || input.type === 'text') {
                            input.value = '';
                        } else if (input.type === 'checkbox') {
                            input.checked = false;
                        }
                    })
                    var allselects = resposta.querySelectorAll('select')
                    allselects.forEach(function (select) {
                        select.value = '';
                    })

                });
            });
        });
    }
}

