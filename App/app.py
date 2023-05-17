from flask import Flask, request, render_template, url_for, redirect
from io import StringIO
from modules.database import mydb, cursor
from modules.template import env
from modules.helpers import rowInRows, rowInRowsFor2Columns, rowInRowsFor3Columns
import modules.queries as q
from modules.blob import blob_service_client, container_name
from datetime import datetime

app = Flask(__name__)

#API to insert into database
@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        server_hostname = request.form['server-hostname']
        file_data = request.files['access-log-file']
        # Create a unique identifier (timestamp-based in this example)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Generate a new blob name using the unique identifier
        file_name = f"{file_data.filename}{timestamp}"
        server_name = (server_hostname,)
        server_name_and_file = (server_hostname, file_name)
        
        cursor.execute(q.create_table_nginx_server_hostname)
        cursor.execute(q.create_table_nginx_logs)
        
        cursor.execute(q.check_server_name_exists, server_name)
        check = cursor.fetchone()[0]
        if check!=1:
            cursor.execute(q.insert_server_name, server_name_and_file)
        
        #BLOB UPLOAD AND DOWNLOAD
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        content_type = file_data.content_type
        blob_client.upload_blob(file_data, content_type=content_type)

        log_data = blob_client.download_blob().content_as_text()
        log_data = StringIO(log_data)

        #Insert nginx-logs into table
        for line in log_data:
            log_data = line.split()
            remote_addr = log_data[0]
            time_local = log_data[1]
            request_method = log_data[3][1:]
            path = log_data[4]
            http_status_code = log_data[6]
            response_time = log_data[7]
            client_ip = log_data[8]
            request_size = log_data[9]
            tls_version = log_data[-5]
            host = log_data[-1]
            val = (server_hostname, remote_addr, time_local, request_method, path, http_status_code, response_time, client_ip, request_size, tls_version, host)
            cursor.execute(q.insert_nginx_logs, val)

        mydb.commit()
        return redirect(url_for('view')) 


#API to VIEW, SEARCH and DELETE log records
@app.route('/view', methods=['GET', 'DELETE'], endpoint='view')
def nginx_log():
    template = env.get_template('App/templates/view.html')

    #DELETE API
    if request.method == 'DELETE':
        deleteQuery = "DELETE FROM nginx_logs WHERE id = %s;"
        deleteParam = (request.args.get('delete'),)
        cursor.execute(deleteQuery, deleteParam)
        mydb.commit()
        return "deleted"
    
    else:
        search_query = str(request.args.get('search'))    
        search_query = "%" + search_query + "%"        
        withSearchVal = (search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query)
        #GET API to VIEW RECORDS
        if search_query == "%None%" or search_query == '':
            cursor.execute(q.view_table_query)   
            rows = cursor.fetchall()

        #GET API to SEARCH RECORDS
        else:
            cursor.execute(q.search_table_query, withSearchVal)   
            rows = cursor.fetchall()

    
        result = rowInRows(rows)    
        html =  template.render(rows=result, search_query = search_query)
        return html

#GET API to VIEW METRICS
@app.route('/metrics', methods=['GET'])
def metrics():
    template = env.get_template('App/templates/metrics.html')    
    metricVal = str(request.args.get('metricParam'))
    
    if metricVal != "None" or metricVal != '':
        result = []
        if metricVal=='byClientIP':
            cursor.execute(q.metric_by_IP)  
            rows = cursor.fetchall()        
            result = rowInRowsFor2Columns(rows)  
        elif metricVal=='byHost':
            cursor.execute(q.metric_by_host)  
            rows = cursor.fetchall()        
            result = rowInRowsFor2Columns(rows)   
        elif metricVal=='byReqSize':
            cursor.execute(q.metric_by_requestsize)  
            rows = cursor.fetchall()        
            result = rowInRowsFor2Columns(rows)   
        elif metricVal=='byHostPath':
            cursor.execute(q.metric_by_host_and_path)  
            rows = cursor.fetchall()        
            result = rowInRowsFor3Columns(rows)   
        elif metricVal=='byRespTime':
            cursor.execute(q.metric_by_responsetime)   
            rows = cursor.fetchall()        
            result = rowInRowsFor2Columns(rows)  
        elif metricVal=='byStatusCode':
            cursor.execute(q.metric_by_statuscode)
            rows = cursor.fetchall()        
            result = rowInRowsFor3Columns(rows)  
        else:
            return template.render(rows=result, metricParam=metricVal)
    
    html =  template.render(rows=result, metricParam=metricVal)
    return html


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)