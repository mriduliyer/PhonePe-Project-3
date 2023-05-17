create_table_nginx_server_hostname = "CREATE TABLE IF NOT EXISTS nginx_server_hostname(server_name VARCHAR(255) PRIMARY KEY, file_name VARCHAR(255));"
create_table_nginx_logs = "CREATE TABLE IF NOT EXISTS nginx_logs (id INT AUTO_INCREMENT PRIMARY KEY,server_name VARCHAR(255) NOT NULL,ip_address VARCHAR(50),timestamp VARCHAR(255),request_method VARCHAR(10),path VARCHAR(255),http_status_code INT,response_time FLOAT,client_ip VARCHAR(50),request_size FLOAT,tls_version VARCHAR(255),host VARCHAR(255), FOREIGN KEY (server_name) REFERENCES nginx_server_hostname(server_name));"

check_server_name_exists = ("SELECT EXISTS(SELECT 1 FROM nginx_server_hostname WHERE server_name = %s);")
insert_server_name = ("INSERT INTO nginx_server_hostname values(%s,%s);")
insert_nginx_logs = "INSERT INTO nginx_logs (server_name, ip_address, timestamp, request_method, path, http_status_code, response_time, client_ip, request_size, tls_version, host) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
view_table_query = "SELECT * FROM nginx_logs;"
search_table_query = "SELECT * FROM nginx_logs WHERE ip_address LIKE %s OR timestamp LIKE %s OR request_method LIKE %s OR path LIKE %s OR http_status_code LIKE %s OR response_time LIKE %s OR client_ip LIKE %s OR request_size LIKE %s OR tls_version LIKE %s OR host LIKE %s"
metric_by_IP = "SELECT client_ip, COUNT(*) AS request_count FROM nginx_logs GROUP BY client_ip ORDER BY request_count DESC LIMIT 5;"
metric_by_host = "SELECT host, COUNT(*) AS request_count FROM nginx_logs GROUP BY host ORDER BY request_count DESC LIMIT 5;"
metric_by_requestsize = "SELECT path, request_size FROM nginx_logs ORDER BY request_size DESC LIMIT 5;"
metric_by_host_and_path = "SELECT host, CONCAT(SUBSTRING_INDEX(SUBSTRING_INDEX(path, '/', 2), '/', -1), '/', SUBSTRING_INDEX(path, '/', -1)) AS path_subdirectories, COUNT(*) FROM nginx_logs GROUP BY host, path ORDER BY COUNT(*) DESC LIMIT 5;"
metric_by_responsetime = "SELECT path, response_time FROM nginx_logs GROUP BY path,response_time ORDER BY response_time DESC LIMIT 5;"
metric_by_statuscode = "SELECT host, http_status_code, COUNT(*) FROM nginx_logs WHERE http_status_code LIKE '200%' OR http_status_code LIKE '4%' OR http_status_code LIKE '5%' GROUP BY host, http_status_code ORDER BY COUNT(*) DESC LIMIT 5;"
