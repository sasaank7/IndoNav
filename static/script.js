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

    var xhr = new XMLHttpRequest();$(document).ready(function() {
    $('#searchForm').submit(function(event) {
        event.preventDefault();
        var source = $('#source').val();
        var destination = $('#destination').val();

        // Perform AJAX request to backend
        $.ajax({
            type: 'POST',
            url: '/get_path',
            data: {source: source, destination: destination},
            success: function(response) {
                displayPath(response.path);
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});

function displayPath(path) {
    var pathDisplay = $('#pathDisplay');
    pathDisplay.empty();
    if (path && path.length > 0) {
        var pathList = $('<ul>');
        path.forEach(function(node) {
            var listItem = $('<li>').text(node);
            pathList.append(listItem);
        });
        pathDisplay.append(pathList);
    } else {
        pathDisplay.text('No path found for the given source.');
    }
}


    xhr.send(JSON.stringify({ source: source, destination: destination }));

});