document.addEventListener("DOMContentLoaded", function () {
    const label = document.querySelector('span.helptext')
    label.remove()

    const p = document.querySelectorAll('p')[3].querySelector('label').textContent = "Confirma password:"
    console.log(p);
})