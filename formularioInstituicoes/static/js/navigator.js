document.addEventListener('DOMContentLoaded', function() {
    let labelsWithValueMinusOne = [];

    var labels = document.querySelectorAll('label');
    console.log(labels)
    // Itera sobre cada checkbox e verifica seu valor
    labels.forEach(function(label) {
        console.log(label.innerText)
        if (label.innerText.trim() === "hidden") {
            label.querySelector('input').checked = true
            label.style.display = 'None'
        }
    });
});














