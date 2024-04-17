function toggle(element) {
    document.querySelectorAll(".bloco").forEach(function (e) {
        e.style.display = "none";
    });
    const bloco = element.nextElementSibling;
    const sinal = element.querySelector("#sinal");
    if (bloco.style.display === "none" || bloco.style.display === "") {
        bloco.style.display = "block";
        sinal.innerText = '-';
    } else {
        bloco.style.display = "none";
        sinal.innerText = '+';
    }
}

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

document.addEventListener("DOMContentLoaded", function () {
    const elementosComPotenciaMedia = document.querySelectorAll('[id*="com-potencia-media-de"]');
    for (const elemento of elementosComPotenciaMedia) {
        elemento.style.display = 'none';
    }

    const checkboxes = document.querySelectorAll('input[type="checkbox"]');

    for (const checkbox of checkboxes) {
        const labelId = checkbox.id;
        const labelElement = document.querySelector(`label[for="${labelId}"]`);
        const labelText = slugify(labelElement.textContent);
        const subtemaNumero = checkbox.closest('.perto').querySelector('h3').textContent.split('.')[0];
        const labelProcurar = `${subtemaNumero}:${labelText}`

        const elementoDiv = document.getElementById(labelProcurar);

        if (elementoDiv) {
            elementoDiv.style.display = 'none';
            console.log(elementoDiv);
        } else {
            console.log('Elemento não encontrado:', labelProcurar);
        }

    }

    for (const checkbox of checkboxes) {
        const labelId = checkbox.id;
        const labelElement = document.querySelector(`label[for="${labelId}"]`);
        const labelText = slugify(labelElement.textContent);
        const subtemaNumero = checkbox.closest('.perto').querySelector('h3').textContent.split('.')[0];
        const labelProcurar = `${subtemaNumero}:${labelText}`
        const elementoDiv = document.getElementById(labelProcurar);


        checkbox.addEventListener('change', function () {
            if (elementoDiv) {
                if (checkbox.checked) {
                    elementoDiv.style.display = 'block';

                    // Set required attribute to true for all question inputs
                    for (const input of questionInputs) {
                        input.setAttribute('required', true);
                    }
                } else {
                    elementoDiv.style.display = 'none';

                    // Remove required attribute for all question inputs
                    for (const input of questionInputs) {
                        input.removeAttribute('required');
                    }
                }
            }

        });
        console.log(elementoDiv)
    }


    for (const checkbox of checkboxes) {

        const labelId = checkbox.id;
        const labelElement = document.querySelector(`label[for="${labelId}"]`);
        const labelText = slugify(labelElement.textContent);

        const subtemaNumero = checkbox.closest('.perto').querySelector('h3').textContent.split(' ')[0];

        const labelProcurar = `${subtemaNumero}:${labelText}-com-potencia-media-de`

        const elementoDiv = document.getElementById(labelProcurar);

        checkbox.addEventListener('change', function () {
            if (elementoDiv) {
                if (checkbox.checked) {
                    elementoDiv.style.display = 'table-row';

                    // Set required attribute to true for all question inputs
                    for (const input of questionInputs) {
                        input.setAttribute('required', true);
                    }
                } else {
                    elementoDiv.style.display = 'none';

                    // Remove required attribute for all question inputs
                    for (const input of questionInputs) {
                        input.removeAttribute('required');
                    }
                }
            }

        });
    }

});


function adicionarValorPergunta() {

    const currentTr = event.target.closest('tr');

    const inputElement = currentTr.querySelector('td#resposta > div#boxResposta > div > p > input');

    const divBoxResposta = currentTr.querySelector('td#resposta > div#boxResposta');

    let unidade = null;

    if (divBoxResposta.childElementCount === 3){
        const divsDentroBoxResposta = divBoxResposta.querySelectorAll('div');
        unidade = divsDentroBoxResposta[1].cloneNode(true);
        console.log(unidade);
    }

    const cloneInputElement = inputElement.cloneNode(true);
    cloneInputElement.value = '';

    var novoItem = document.createElement('div');
    novoItem.id = 'boxRespostaNova';

    var novoDiv = document.createElement('div');
    var novoDiv2 = document.createElement('div');
    var novoP = document.createElement('p');

    var novoInput = cloneInputElement;
    novoInput.type = 'text'; // Define o tipo do input
    novoInput.className = 'input-resposta'; // Adiciona uma classe ao input

    var botaoRemover = document.createElement('button');
    botaoRemover.type = 'button';
    botaoRemover.className = 'butao_remove'; // Adiciona uma classe ao botão
    botaoRemover.innerText = '-'; // Define o texto do botão

    botaoRemover.addEventListener('click', function () {
        // Remove o div pai do botão (que contém o input e o botão)
        const divPai = this;
        const divBoxResposta = divPai.closest('#boxRespostaNova');

        console.log(divBoxResposta)
        divBoxResposta.remove();

    });

    novoItem.appendChild(novoDiv).appendChild(novoP).appendChild(novoInput);

    if(unidade != null){

        novoItem.appendChild(unidade);
    }

    novoItem.appendChild(novoDiv2).appendChild(botaoRemover);

    const currentRow = currentTr.id.split(':')[1];

    var listaValoresDiv = document.getElementById(currentRow);
    listaValoresDiv.appendChild(novoItem);
}










