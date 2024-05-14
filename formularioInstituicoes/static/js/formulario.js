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

function checkboes_display() {
    const elementosComPotenciaMedia = document.querySelectorAll('[id*="com-potencia-media-de"]');
    for (const elemento of elementosComPotenciaMedia) {
        elemento.style.display = 'none';
    }

    const checkboxes = document.querySelectorAll('input[type="checkbox"]');

    for (const checkbox of checkboxes) {
        const labelId = checkbox.id;
        const labelElement = document.querySelector(`label[for="${labelId}"]`);
        const labelText = slugify(labelElement.textContent);
        const subtemaNumero = checkbox.closest('.bloco_subtema').querySelector('h3').textContent.split('.')[0];
        const labelProcurar = `${subtemaNumero}:${labelText}`

        const elementoDiv = document.getElementById(labelProcurar);

        if (elementoDiv) {
            elementoDiv.style.display = 'none';
        }

    }

    for (const checkbox of checkboxes) {
        const labelId = checkbox.id;
        const labelElement = document.querySelector(`label[for="${labelId}"]`);
        const labelText = slugify(labelElement.textContent);
        const subtemaNumero = checkbox.closest('.bloco_subtema').querySelector('h3').textContent.split('.')[0];
        const labelProcurar = `${subtemaNumero}:${labelText}`
        const elementoDiv = document.getElementById(labelProcurar);

        if (elementoDiv) {
            if (checkbox.checked === true) {
                elementoDiv.style.display = 'block';
            }
        }


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
    }


    for (const checkbox of checkboxes) {
        const labelId = checkbox.id;
        const labelElement = document.querySelector(`label[for="${labelId}"]`);
        const labelText = slugify(labelElement.textContent);

        const subtemaNumero = checkbox.closest('.bloco_subtema').querySelector('h3').textContent.split(' ')[0];

        const labelProcurar = `${subtemaNumero}:${labelText}-com-potencia-media-de`

        const elementoDiv = document.getElementById(labelProcurar);

        if (elementoDiv) {
            if (checkbox.checked === true) {
                elementoDiv.style.display = 'table-row';
            }
        }

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
}

document.addEventListener("DOMContentLoaded", function () {
    checkboes_display();
});


function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

window.onload = function () {
    var id_tema = getParameterByName('id');
    var string = 'temaID:' + id_tema

    const div_titulo = document.getElementById(string)

    const div_bloco = div_titulo.closest('div.tema').querySelector('div.bloco')
    div_bloco.style.display = 'block'
}


function toggle(element) {
    document.querySelectorAll(".bloco").forEach(function (e) {
        e.style.display = "none"
        e.closest('div.tema').querySelector('div.titulo').querySelector('span#sinal').innerText = "+"
    });

    const bloco = element.nextElementSibling;
    const sinal = element.querySelector("#sinal");

    if (bloco.style.display === "none" || bloco.style.display === "") {
        bloco.style.display = "block";
        sinal.innerText = '-';
    }

    var scrollPosition = bloco.offsetTop - 170;

    window.scrollTo({
        top: scrollPosition,
        behavior: "smooth"
    })
}

function adicionarValorPergunta() {

    const currentTr = event.target.closest('tr');

    const inputElement = currentTr.querySelector('td#resposta > div#boxResposta > div > p > input');

    const divBoxResposta = currentTr.querySelector('td#resposta > div#boxResposta');

    let unidade = null;

    if (divBoxResposta.childElementCount === 3) {
        const divsDentroBoxResposta = divBoxResposta.querySelectorAll('div');
        unidade = divsDentroBoxResposta[1].cloneNode(true);
    }

    const cloneInputElement = inputElement.cloneNode(true);

    cloneInputElement.value = '';

    var novoItem = document.createElement('div');
    novoItem.id = 'boxRespostaNova';

    var novoDiv = document.createElement('div');
    var novoDiv2 = document.createElement('div');
    var novoP = document.createElement('p');

    var novoInput = cloneInputElement;
    novoInput.type = 'text';
    novoInput.className = 'input-resposta';

    var botaoRemover = document.createElement('button');
    botaoRemover.type = 'button';
    botaoRemover.className = 'butao_remove';
    botaoRemover.innerText = '-';

    botaoRemover.addEventListener('click', function () {
        const divPai = this;
        const divBoxResposta = divPai.closest('#boxRespostaNova');
        divBoxResposta.remove();

    });

    novoItem.appendChild(novoDiv).appendChild(novoP).appendChild(novoInput);

    if (unidade != null) {

        novoItem.appendChild(unidade);
    }

    novoItem.appendChild(novoDiv2).appendChild(botaoRemover);

    var listaValoresDiv = document.getElementById(currentTr.id).querySelector('#resposta');
    listaValoresDiv.style.display = 'block'
    listaValoresDiv.appendChild(novoItem);
}

function adicionarValorSubtema() {
    const currentDiv = event.target.closest('div');

    const currentDivClone = currentDiv.cloneNode(true);
    const inputElements = currentDivClone.querySelectorAll('input');
    inputElements.forEach(input => input.value = '');


    currentDivClone.querySelector('h3 > button').remove()

    var botaoRemover = document.createElement('button');
    botaoRemover.type = 'button';
    botaoRemover.className = 'butao_remove';
    botaoRemover.innerText = '-';

    botaoRemover.addEventListener('click', function () {

        const currentDiv = event.target.closest('div');
        currentDiv.remove()

    });

    currentDivClone.querySelector('h3').appendChild(botaoRemover)

    const closestForm = event.target.closest('form');
    const submitButton = closestForm.querySelector('input[type="submit"]');

    closestForm.appendChild(currentDivClone);
    closestForm.appendChild(submitButton);

}

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

