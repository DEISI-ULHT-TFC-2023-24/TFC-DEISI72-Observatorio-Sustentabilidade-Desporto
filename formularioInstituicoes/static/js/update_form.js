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


