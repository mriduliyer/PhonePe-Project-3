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
    window.location.href = '/view?search=' + searchInput;
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
    fetch('/view?delete=' + row_id,
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