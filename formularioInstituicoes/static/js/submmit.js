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

        var respostas_usadas = div_valor_relevante.querySelectorAll('table > tbody > tr > td#resposta > div#boxResposta > div > div');

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

        var form_subtemas = div_valor_relevante.closest("form").querySelectorAll("div.bloco_subtema")

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

        var resposta_dada_div = resposta_dada_div_first.querySelectorAll('td#resposta > div#boxResposta > div > div')

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
            console.log(perguntas)
        }





    }

};