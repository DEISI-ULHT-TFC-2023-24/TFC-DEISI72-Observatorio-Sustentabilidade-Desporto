document.addEventListener('DOMContentLoaded', function() {
    let labelsWithValueMinusOne = [];

    var labels = document.querySelectorAll('label');
    // Itera sobre cada checkbox e verifica seu valor
    labels.forEach(function(label) {
        if (label.innerText.trim() === "hidden") {
            label.querySelector('input').checked = true
            label.style.display = 'None'
        }
    });
});

function getValorInstalacaoFromURL() {

    var url = window.location.href;
    console.log(url)
    var valor_instalacao = url.lastIndexOf("=");
    return url.substring(valor_instalacao + 1);
}

function form_link(){
    var instalacao = getValorInstalacaoFromURL();
    window.location.href = `/form?instalacao=${instalacao}`;
}

function submmit_link(){
    var instalacao = getValorInstalacaoFromURL();
    window.location.href = `/submmit?instalacao=${instalacao}`;
}

function dash_link(){
    var instalacao = getValorInstalacaoFromURL();
    window.location.href = `/dashboard_energia?instalacao=${instalacao}`;
}














