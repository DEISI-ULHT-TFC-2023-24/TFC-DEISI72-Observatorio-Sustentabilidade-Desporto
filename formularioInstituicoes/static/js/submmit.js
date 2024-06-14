function slugify(texto) {
    const caracteresEspeciais = {
        á: 'a',
        é: 'e',
        í: 'i',
        ó: 'o',
        ú: 'u',
        à: 'a',
        è: 'e',
        ì: 'i',
        ò: 'o',
        ù: 'u',
        â: 'a',
        ê: 'e',
        î: 'i',
        ô: 'o',
        û: 'u',
        ã: 'a',
        õ: 'o',
        ç: 'c',
        ñ: 'n',
        ä: 'a',
        ë: 'e',
        ï: 'i',
        ö: 'o',
        ü: 'u',
        Á: 'A',
        É: 'E',
        Í: 'I',
        Ó: 'O',
        Ú: 'U',
        À: 'A',
        È: 'E',
        Ì: 'I',
        Ò: 'O',
        Ù: 'U',
        Â: 'A',
        Ê: 'E',
        Î: 'I',
        Ô: 'O',
        Û: 'U',
        Ã: 'A',
        Õ: 'O',
        Ç: 'C',
        Ñ: 'N',
        Ä: 'A',
        Ë: 'E',
        Ï: 'I',
        Ö: 'O',
        Ü: 'U',
    };

    return texto.toString().toLowerCase()
        .replace(/\s+/g, '-') // Substitui espaços por -
        .replace(/[\-]/g, ' ') // Substitui hifens por espaços temporariamente
        .replace(/\s+/g, '-') // Substitui espaços por -
        .replace(/\-{2,}/g, '-') // Substitui hifens duplicados por um único hífen
        .replace(/^\-+/, '') // Remove hifens do início do texto
        .replace(/\-+$/, '') // Remove hifens do final do texto
        .replace(/[^\w\s-]/g, (caractere) => caracteresEspeciais[caractere] || caractere);
}

window.onload = function () {
    const valores_relevantes_h3 = document.querySelectorAll('[id="valores-relevantes"]');
    for (const valor_relevante of valores_relevantes_h3) {
        var div_valor_relevante = valor_relevante.closest("div")

        var respostas_usadas = div_valor_relevante.querySelectorAll('table > tbody > tr > td#resposta > div#boxResposta > div > div > span');

        var lista_valores_nao_esconder = []

        for (const resposta_usada of respostas_usadas) {

            const childNodes = resposta_usada.childNodes;

            let texto = '';
            childNodes.forEach(node => {
                if (node.nodeType === Node.TEXT_NODE) {
                    texto += node.textContent.trim();
                }
            });

            if (texto !== "Não respondeu") {
                lista_valores_nao_esconder.push([texto, false])
            }
        }


        var numero_pergunta = div_valor_relevante.id.split(":")[0]

        var form_subtemas = div_valor_relevante.closest("div.bloco").querySelectorAll("div.bloco_subtema")
        for (const subtema of form_subtemas) {
            if (subtema.id !== `${numero_pergunta}:valores-relevantes`) {
                subtema.style.display = 'none'
            }

        }

        for (const subtema of form_subtemas) {
            lista_valores_nao_esconder.forEach(item => {
                var id_procurar = slugify(`${numero_pergunta}:${item[0]}`)
                if (item[1] === false) {
                    if (subtema.id === id_procurar) {
                        subtema.style.display = 'block'
                        item[1] = true
                    }
                }
            })
        }
    }

    const potencia_media_pergunta = document.querySelectorAll('tr[id*="com-potencia-media-de"]');

    for (const pergunta_tr of potencia_media_pergunta) {
        var div_subtema = pergunta_tr.closest(".bloco_subtema")

        var resposta_dada_div_first = div_subtema.querySelectorAll('table > tbody > tr')[0]

        var resposta_dada_div = resposta_dada_div_first.querySelectorAll('td#resposta > div#boxResposta > div > div > span')

        lista_valores_nao_esconder = []

        for (const resposta of resposta_dada_div) {
            const childNodes = resposta.childNodes;

            let texto = '';
            childNodes.forEach(node => {
                if (node.nodeType === Node.TEXT_NODE) {
                    texto += node.textContent.trim();
                }
            });

            lista_valores_nao_esconder.push([texto, false])
        }

        pergunta_tr_mudar = div_subtema.querySelectorAll('table > tbody > tr')
        for (const perguntas of pergunta_tr_mudar) {
            perguntas.style.display = 'none'
        }

        pergunta_tr_mudar[0].style.display = 'block'

        for (const perguntas of pergunta_tr_mudar) {
            lista_valores_nao_esconder.forEach(item => {

                var id_procurar_split = slugify(`${item[0]}-com-potencia-media-de`)
                if (item[1] === false) {
                    if (perguntas.id.split(":")[1] === id_procurar_split) {
                        perguntas.style.display = 'block'
                        item[1] = true
                    }
                }
            })
        }
    }

    const as = document.querySelectorAll('a');
    as.forEach(function (a) {
        const innertxt = a.innerText.split('\\')
        const tamanho = innertxt.length
        if (tamanho > 1) {
            a.innerText = 'Ficheiro'
        }
    });
};

document.addEventListener("DOMContentLoaded", function () {
    const botoes_editar = document.querySelectorAll('button.botao_submmit')

    for (const botao of botoes_editar) {
        botao.style.display = "none"
    }
})

function toggle(element) {
    document.querySelectorAll(".bloco").forEach(function (e) {
        e.style.display = "none";
        e.closest('div.tema').querySelector('div.titulo').querySelector('button').style.display = "none";
        e.closest('div.tema').querySelector('div.titulo').querySelector('span#sinal').innerText = "+";
    });

    const bloco = element.nextElementSibling;
    const sinal = element.querySelector("#sinal");

    const button = bloco.closest('div.tema').querySelector('div.titulo').querySelector('button');

    if (bloco.style.display === "none" || bloco.style.display === "") {
        bloco.style.display = "block";
        sinal.innerText = '-';
        button.style.display = "inline";


        var scrollPosition = bloco.offsetTop - 170;

        window.scrollTo({
            top: scrollPosition,
            behavior: "smooth"
        })
    }
}


function editar(csrftoken, tema_id) {

    const requestObj = new XMLHttpRequest()

    requestObj.open("POST", '/post/')
    requestObj.setRequestHeader("X-CSRFToken", csrftoken)

    const formdata = new FormData()
    formdata.append('metodo', 'post')
    formdata.append('tipo_query', 'editar')
    requestObj.send(formdata)

    const params = new URLSearchParams(window.location.search);
    const instalacao = params.get('instalacao');

    window.location.href = `/update_form/${tema_id}?instalacao=${instalacao}`;

}

function remover(csrftoken, resposta_id, tipo_resposta) {
    const requestObj = new XMLHttpRequest()

    requestObj.open("POST", '/post/')
    requestObj.setRequestHeader("X-CSRFToken", csrftoken)

    const formdata = new FormData()
    formdata.append('metodo', 'post')
    formdata.append('tipo_query', 'remover')
    formdata.append('tipo_resposta', tipo_resposta)
    formdata.append('id_resposta', resposta_id);
    requestObj.send(formdata)

    var div_element = document.getElementById(`botao_remover:${resposta_id}`).closest('div#resposta_dada')

    var texto_pergunta = div_element.querySelector('span').textContent

    var subtema_pergunta = div_element.closest('div.bloco_subtema').closest('div.bloco_subtema').querySelector('h3').id

    var div_tema = div_element.closest('div.bloco_subtema').closest('div.tema')
    var div_subtemas_todos = div_tema.querySelectorAll('div.bloco > div.bloco_subtema')
    var subtema_esconder = slugify(texto_pergunta)

    var perguntas_not_hidden = []
    var subtemas_not_hidden = []

    var div_subtemas_perguntas = div_tema.querySelectorAll('div.bloco > div')

    for (const div_subtema of div_subtemas_perguntas) {
        var id_pergunta = div_subtema.id.split(":")[1]
        if (id_pergunta === subtema_pergunta) {
            var tr_perguntas = div_subtema.querySelectorAll('table > tbody > tr')
            for (const tr_pergunta of tr_perguntas) {
                if (tr_pergunta.id.includes('-com-potencia-media-de')) {
                    if (tr_pergunta.style.display !== 'none') {
                        perguntas_not_hidden.push(tr_pergunta)
                    }
                }
            }
        }
    }

    for (let i = 0; i < div_subtemas_todos.length; i++) {
        const div_subtema_cada = div_subtemas_todos[i];
        if (i !== 0 && div_subtema_cada.style.display !== 'none') {
            console.log(div_subtema_cada)
            subtemas_not_hidden.push(div_subtema_cada);
        }
    }

    if (subtemas_not_hidden.length !== 0) {
        if (subtemas_not_hidden.length <= 1) {
            div_element.querySelectorAll('button')[1].remove()
            div_element.querySelector('span').textContent = "Não Respondeu"
        } else {
            div_element.remove()
        }
    } else if (perguntas_not_hidden.length !== 0) {
        if (perguntas_not_hidden.length <= 1) {
            div_element.querySelectorAll('button')[1].remove()
            div_element.querySelector('span').textContent = "Não Respondeu"
        } else {
            div_element.remove()
        }
    } else {
        div_element.querySelectorAll('button')[1].remove()
        div_element.querySelector('span').textContent = "Não Respondeu"
    }


    for (const div_subtema_cada of div_subtemas_todos) {

        if (div_subtema_cada.querySelector('h3').id === subtema_esconder) {
            div_subtema_cada.style.display = 'none'
        }
    }

    for (const div_subtema of div_subtemas_perguntas) {
        var id_pergunta = div_subtema.id.split(":")[1]
        if (id_pergunta === subtema_pergunta) {
            var tr_perguntas = div_subtema.querySelectorAll('table > tbody > tr')
            for (const tr_pergunta of tr_perguntas) {
                if (slugify(tr_pergunta.id.split('-com-potencia-media-de')[0].split(':')[1]) === slugify(texto_pergunta)) {
                    tr_pergunta.style.display = 'none'
                }
            }
        }
    }
}

function submmit(csrftoken) {

    let popup = document.getElementsByClassName('submeterpopup')[0];
    popup.style.visibility = "visible"

    const submmitButton = popup.querySelectorAll('button')[1]

    function handleClick() {

        const instalacao = new URLSearchParams(window.location.search).get('instalacao');

        const requestObj = new XMLHttpRequest()

        requestObj.open("POST", '/post/')
        requestObj.setRequestHeader("X-CSRFToken", csrftoken)

        const formdata = new FormData()
        formdata.append('instalacao', instalacao)
        requestObj.send(formdata)
        window.location.reload();
    }

    submmitButton.addEventListener('click', handleClick);

}

function esconder() {
    let popup = document.getElementsByClassName('submeterpopup')[0];
    popup.style.visibility = "hidden"

}