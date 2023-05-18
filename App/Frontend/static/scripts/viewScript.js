var row_id;
function sortTable(columnIndex) {
    var table = document.getElementById('myTable');
    var tbody = table.querySelector('tbody');
    var rows = Array.from(table.rows);
    rows = rows.slice(1)
    rows.sort(function (a, b) {
        var cellA = a.cells[columnIndex].textContent.toLowerCase();
        var cellB = b.cells[columnIndex].textContent.toLowerCase();

        if (columnIndex == 0) {
            cellA = parseInt(cellA)
            cellB = parseInt(cellB)
        }

        else if (columnIndex == 5) {
            cellA = cellA.split("/").slice(0, 3).join("/");
            cellB = cellB.split("/").slice(0, 3).join("/");
        }
        if (cellA < cellB) {
            return -1;
        }
        else if (cellA > cellB) {
            return 1;
        }
        return 0;
    });

    // Remove existing table rows
    while (table.rows.length > 1) {
        table.deleteRow(1);
    }

    // Re-insert sorted rows
    for (var i = 0; i < rows.length; i++) {
        table.appendChild(rows[i]);
    }
}

function search() {
    var searchInput = document.getElementById('searchInput').value;
    window_loc = 'http://localhost:5001/view?search=' + searchInput;

    // Fetch data from Flask backend and display in the table body
    fetch(window_loc)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('tableBody');
            let tableHtml = '';

            data.forEach((row, index) => {
                console.log('Row:', row);
                tableHtml += `
                        <tr onclick="getRowId(${row.index})">
                            <td>${row.index}</td>
                            <td>${row.server_hostname}</td>
                            <td>${row.IP_address}</td>
                            <td>${row.timestamp}</td>
                            <td>${row.request_method}</td>
                            <td>${row.path}</td>
                            <td>${row.http_status_code}</td>
                            <td>${row.response_time}</td>
                            <td>${row.client_ip}</td>
                            <td>${row.request_size}</td>
                            <td>${row.tls_version}</td>
                            <td>${row.host}</td>
                        </tr>
                    `;
            });

            tableBody.innerHTML = tableHtml;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function enableDeleteButton() {
    var deleteButton = document.getElementById('deleteButton');
    deleteButton.disabled = false;
}

function getRowId(id) {
    enableDeleteButton();
    row_id = id;
}

function deleteRecord() {
    fetch('http://localhost:5001/view?delete=' + row_id,
        {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                // Successful deletion
                window.location.href = '/view'; // Redirect to the same page
            }
            else {
                // Error handling
                console.error('Error deleting record:', response.status, response.statusText);
            }
        })
        .catch(error => {
            // Error handling
            console.error('Error deleting record:', error);
        });
}

fetch('http://localhost:5001/view')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.getElementById('tableBody');
        let tableHtml = '';
        data.forEach((row, index) => {
            console.log('Row:', row);
            tableHtml += `
            <tr onclick="getRowId(${row.index})">
              <td>${row.index}</td>
              <td>${row.server_hostname}</td>
              <td>${row.IP_address}</td>
              <td>${row.timestamp}</td>
              <td>${row.request_method}</td>
              <td>${row.path}</td>
              <td>${row.http_status_code}</td>
              <td>${row.response_time}</td>
              <td>${row.client_ip}</td>
              <td>${row.request_size}</td>
              <td>${row.tls_version}</td>
              <td>${row.host}</td>
            </tr>
          `;
        });

        tableBody.innerHTML = tableHtml;
        dataLoaded = true;
    })
    .catch(error => {
        console.error('Error:', error);
    });


