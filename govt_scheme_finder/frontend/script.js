document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/latest-schemes')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('latest-schemes-container');
            container.innerHTML = 'Latest schemes will be displayed here.';
            // Logic to render latest schemes will go here
        });

    fetch('/api/schemes')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('all-schemes-container');
            container.innerHTML = 'All schemes will be displayed here.';
            // Logic to render all schemes will go here
        });
});
