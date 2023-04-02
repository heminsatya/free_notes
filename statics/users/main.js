// Timout variable for alert messages
let timeout = null;

// Document loaded
document.addEventListener('DOMContentLoaded', function() {

    // Register form
    const register_form = document.querySelector('#register-form');
    if (register_form) {
        // Result container
        const result_div = document.querySelector('#result');

        // Handle form submit
        const submit_button = document.querySelector('#register-form .submit');
        register_form.onsubmit = function () {
            clearTimeout(timeout);
            
            // Prepare the submit button
            submit_button.setAttribute("disabled", true);
            submit_button.innerHTML = "Requesting...";

            // Form date
            const action = this.getAttribute('action');
            const method = this.getAttribute('method');
            const data = new FormData(this);

            // Submit form data via fetch API
            fetch(action, {
                method: method,
                body: data,
            })
            .then(response => response.json())
            .then(result => {
                // Display the result container
                result_div.style.display = 'block';

                // An error occoured
                if (result.error) {
                    result_div.innerHTML = `<div class="alert-app-light">${result.error}</div>`;

                    // Reset the submit button
                    submit_button.removeAttribute("disabled");
                    submit_button.innerHTML = "Register";
                }

                // Everything is fine
                else if (result.success) {
                    // Show message
                    result_div.innerHTML = `<div class="alert-app-light">${result.success}</div>`;
                    
                    // Reset the form
                    this.reset();
            
                    // Reset the submit button
                    submit_button.innerHTML = "Register";

                    // Redirect to index after 1 second
                    setTimeout(function() {
                        window.location.href = '/';
                    }, 1000);
                }

                // Hide result
                timeout = setTimeout(() => {
                    result_div.innerHTML = '';
                    result_div.style.display = '';
                }, 5000);
            });

            // Prevent default behavior
            return false

        };
    }

    
    // Login form
    const login_form = document.querySelector('#login-form');
    if (login_form) {
        // Result container
        const result_div = document.querySelector('#result');

        // Handle form submit
        const submit_button = document.querySelector('#login-form .submit');
        login_form.onsubmit = function () {
            clearTimeout(timeout);
            
            // Prepare the submit button
            submit_button.setAttribute("disabled", true);
            submit_button.innerHTML = "Requesting...";
            
            // Form date
            const action = this.getAttribute('action');
            const method = this.getAttribute('method');
            const data = new FormData(this);

            // Submit form data via fetch API
            fetch(action, {
                method: method,
                body: data,
            })
            .then(response => response.json())
            .then(result => {
                
                // Display the result container
                result_div.style.display = 'block';

                // An error occoured
                if (result.error) {
                    result_div.innerHTML = `<div class="alert-app-light">${result.error}</div>`;

                    // Reset the submit button
                    submit_button.removeAttribute("disabled");
                    submit_button.innerHTML = "Login";
                }

                // Everything is fine
                else if (result.success) {
                    // Show message
                    result_div.innerHTML = `<div class="alert-app-light">${result.success}</div>`;
                    
                    // Reset the form
                    this.reset();

                    // Reset the submit button
                    submit_button.innerHTML = "Login";

                    // Redirect to index/next after 1 second
                    setTimeout(function() {
                        window.location.href = `${result.url}`;
                    }, 1000);
                }

                // Hide result
                timeout = setTimeout(() => {
                    result_div.innerHTML = '';
                    result_div.style.display = '';
                }, 5000);
            });

            // Prevent default behavior
            return false

        };
    }

});