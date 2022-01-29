// Timout variable for alert messages
let timeout = null;

// Document loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // New note form
    const new_note_form = document.querySelector('#new-note-form');
    if (new_note_form) {
                    
        // Load Summernote
        $('#dynamic-content').summernote({
            placeholder: '',
            tabsize: 2,
            height: 275
        });
        $('#dynamic-content'). summernote('code', '');

        // Result container
        const result_div = document.querySelector('#result');

        // Handle form submit
        const submit_button = document.querySelector('#new-note-form .submit');
        const dynamic_content = document.querySelector('#dynamic-content');
        new_note_form.onsubmit = function () {
            clearTimeout(timeout);

            // Check content
            if (!dynamic_content.value) {
                // Display the result container
                result_div.style.display = 'block';
                result_div.innerHTML = `<div class="alert-app"><i class="fas fa-exclamation-circle mr-1"></i> The content is required!</div>`;

                // Hide result
                timeout = setTimeout(() => {
                    result_div.innerHTML = '';
                    result_div.style.display = '';
                }, 5000);

                // Prevent form submit
                return false
            }
            
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
                    result_div.innerHTML = `<div class="alert-app">${result.error}</div>`;
                }

                // Everything is fine
                else if (result.success) {
                    // Show message
                    result_div.innerHTML = `<div class="alert-app">${result.success}</div>`;
                    
                    // Reset the form
                    this.reset();

                    // Reset Summernote
                    $('#dynamic-content'). summernote('code', ''); 
                }

                // Reset the submit button
                submit_button.removeAttribute("disabled");
                submit_button.innerHTML = "Submit";

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
    
    // Edit note form
    const edit_note_form = document.querySelector('#edit-note-form');
    if (edit_note_form) {
                    
        // Load Summernote
        $('#dynamic-content').summernote({
            placeholder: '',
            tabsize: 2,
            height: 275
        });

        // Result container
        const result_div = document.querySelector('#result');

        // Handle form submit
        const submit_button = document.querySelector('#edit-note-form .submit');
        const dynamic_content = document.querySelector('#dynamic-content');
        edit_note_form.onsubmit = function () {
            clearTimeout(timeout);

            // Check content
            if (!dynamic_content.value) {
                // Display the result container
                result_div.style.display = 'block';
                result_div.innerHTML = `<div class="alert-app"><i class="fas fa-exclamation-circle mr-1"></i> The content is required!</div>`;

                // Hide result
                timeout = setTimeout(() => {
                    result_div.innerHTML = '';
                    result_div.style.display = '';
                }, 5000);

                // Prevent form submit
                return false
            }
            
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
                    result_div.innerHTML = `<div class="alert-app">${result.error}</div>`;
                }

                // Everything is fine
                else if (result.success) {
                    // Show message
                    result_div.innerHTML = `<div class="alert-app">${result.success}</div>`;
                }

                // Reset the submit button
                submit_button.removeAttribute("disabled");
                submit_button.innerHTML = "Submit";

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


    // My notes
    const my_notes = document.querySelector("#my-notes");
    if (my_notes) {
        // Delete actions
        const popover_open = document.querySelectorAll(".popover-open");
        const popover_close = document.querySelectorAll(".popover-close");
        const action_delete = document.querySelectorAll(".action-delete");
        
        // Open popover 
        popover_open.forEach((elem) => {
            $(`#delete-${elem.dataset.id}`).popover({
                container: 'body',
                title: 'Arue You Sure?',
                content: document.querySelector(`#container-${elem.dataset.id}`),
                placement: 'top',
                html: true,
                trigger: 'click'
            })
        });

        // Close popover
        popover_close.forEach((elem) => {
            elem.onclick = () => {
                $(`#delete-${elem.dataset.id}`).popover('hide');
            }
        });

        // Delete action
        action_delete.forEach((elem) => {
            elem.onclick = () => {
                // Start delete process
                DeleteNoteAPI(elem.dataset.id);
            
            }
        });
    }

});


// Delete Note
function DeleteNoteAPI(note_id) {
    // Result container
    const result_div = document.querySelector('#result');

    // Submit button
    const submit_button = document.querySelector(`#container-${note_id} .action-delete`);
            
    // Prepare the submit button
    submit_button.setAttribute("disabled", true);
    submit_button.innerHTML = "Requesting...";
    
    // Request the process
    fetch('/notes/my-notes/', {
        method: 'DELETE',
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
        body: JSON.stringify({
            id: note_id
        })
    })
    .then(response => response.json())
    .then(result => {
        result_div.style.display = "block";

        // Error occoured
        if (result.error) {
            // Show error
            result_div.innerHTML = `<div class="alert alert-app">${result.error}</div>`;
        
            // Reset the submit button
            submit_button.removeAttribute("disabled");
            submit_button.innerHTML = "Yes";
    
            // Close popover
            $(`#delete-${note_id}`).popover('hide');
        }
        // Everything is fine
        else {
            // Show message
            result_div.innerHTML = `<div class="alert alert-app">${result.success}</div>`;
        
            // Reset the submit button
            submit_button.removeAttribute("disabled");
            submit_button.innerHTML = "Yes";
    
            // Close popover
            $(`#delete-${note_id}`).popover('hide');

            // Remove the deleted tr
            document.querySelector(`#tr-${note_id}`).innerHTML = "";
            document.querySelector(`#tr-${note_id}`).style.display = "";
        }

        // Hide result
        timeout = setTimeout(() => {
            result_div.innerHTML = '';
            result_div.style.display = '';
        }, 5000);
    });
}