window.addEventListener('DOMContentLoaded', function () {
    var urlParams = new URLSearchParams(window.location.search);
    var metricParam = urlParams.get('metricParam');
    if (metricParam) {
        displayMetrics(metricParam);
    }
});
function updateMetricParam(id) {
    window.location.href = '/metrics?metricParam=' + id;
}
function displayMetrics(id) {
    var displayText = document.getElementById('defaultText');
    displayText.style.display = 'none';

    var tables = document.getElementsByClassName('metricTable');
    for (var i = 0; i < tables.length; i++) {
        tables[i].style.display = 'none';
    }

    var metricTable = document.getElementById(id);
    metricTable.style.display = 'block';
}