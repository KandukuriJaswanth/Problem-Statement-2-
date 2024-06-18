fetch('/api/index.html')

    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const statusDiv = document.getElementById('status');
        if (data.message && data.message.includes('up')) {
            statusDiv.innerText = 'Application is up and running.';
            statusDiv.className = 'status up';
        } else {
            statusDiv.innerText = `Application is down. ${data.message || ''}`;
            statusDiv.className = 'status down';
        }
    })
    .catch(error => {
        const statusDiv = document.getElementById('status');
        statusDiv.innerText = `Error: ${error}`;
        statusDiv.className = 'status down';
    });
