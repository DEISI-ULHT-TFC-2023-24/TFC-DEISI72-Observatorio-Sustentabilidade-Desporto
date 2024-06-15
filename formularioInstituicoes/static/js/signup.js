document.addEventListener("DOMContentLoaded", function () {
    // const label = document.querySelector('span.helptext')
    // label.remove()

    document.querySelectorAll('p')[3].querySelector('label').textContent = "Confirma password:"

    const errorMessages = document.querySelectorAll('ul.errorlist')

    if (errorMessages) {

        errorMessages.forEach(function (error) {
            const errorContainer = document.createElement('div');
            errorContainer.classList.add('error-popup');

            // Create a close button
            const closeButton = document.createElement('button');
            closeButton.innerHTML = '&times;';
            closeButton.classList.add('close-button');

            // Append the error message and the close button to the container
            errorContainer.appendChild(error.cloneNode(true));
            errorContainer.appendChild(closeButton);

            // Append the container to the error container in the HTML
            document.getElementById('error-container').appendChild(errorContainer);

            // Remove the original error message from the ul
            error.remove();

            // Add event listener to close the error popup when the button is clicked
            closeButton.addEventListener('click', function () {
                errorContainer.remove();
            });
        })


    }

    const loginForm = document.querySelector('div.loginform');

    if (loginForm) {
        loginForm.scrollIntoView({behavior: 'smooth'});
    }

})