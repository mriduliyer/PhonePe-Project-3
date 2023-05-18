function displayMetrics(div_id, tbody_id) {
    var displayText = document.getElementById('defaultText');
    displayText.style.display = 'none';

    var tables = document.getElementsByClassName('metricTable');
    for (var i = 0; i < tables.length; i++) {
        tables[i].style.display = 'none';
    }

    var metricTable = document.getElementById(div_id);
    metricTable.style.display = 'block';
    window_loc = 'http://localhost:5001/metrics?metricParam=' + div_id;

    if (div_id == 'byClientIP' || div_id == 'byHost' || div_id == 'byReqSize' || div_id == 'byRespTime') {
        fetch(window_loc)
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById(tbody_id);
                let tableHtml = '';

                data.forEach((row, index) => {
                    console.log('Row:', row);
                    tableHtml += `
                <tr>
                    <td>${row.row1}</td>
                    <td>${row.row2}</td>                            
                </tr>
            `;
                });

                tableBody.innerHTML = tableHtml;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    else {
        fetch(window_loc)
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById(tbody_id);
                let tableHtml = '';

                data.forEach((row, index) => {
                    console.log('Row:', row);
                    tableHtml += `
                <tr>
                    <td>${row.row1}</td>
                    <td>${row.row2}</td> 
                    <td>${row.row3}</td>                            
                </tr>
            `;
                });

                tableBody.innerHTML = tableHtml;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
}