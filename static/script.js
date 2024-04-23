/*
document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var source = document.getElementById('source').value;
    var destination = document.getElementById('destination').value;

    // Perform AJAX request to backend
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/get_path', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                displayPath(response.path);
            } else {
                console.error('Error:', xhr.status);
            }
        }
    };
    xhr.send(JSON.stringify({ source: source, destination: destination }));
});
*/
document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var source = document.getElementById('source').value;
    var destination = document.getElementById('destination').value;

    var xhr = new XMLHttpRequest();

    xhr.send(JSON.stringify({ source: source, destination: destination }));

});