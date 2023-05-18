document.getElementById('log_form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission behavior

    var form = document.getElementById('log_form');
    var formData = new FormData(form); // Create a FormData object

    // Make a POST request using the Fetch API
    fetch('http://localhost:5001/postapi', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            if (response.ok) {
                // POST request successful, load the /view page
                window.location.href = '/view';
            } else {
                // Handle error response
                console.error('Error:', response.status, response.statusText);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});