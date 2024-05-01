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













