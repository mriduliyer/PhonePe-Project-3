document.getElementById('log-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission behavior

    var form = document.getElementById('log-form');
    var formData = new FormData(form); // Create a FormData object
    window.location.replace('/view');
    // Make a POST request using the Fetch API
    fetch('http://localhost:5001/postapi', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Process the response as needed
        })
        .catch(error => {
            console.error('Error:', error);
        });
});