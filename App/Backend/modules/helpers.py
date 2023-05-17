def rowInRows(rows):
    result_list = []
    for row in rows:
        dict_row = {
            'index' : row[0],
            'server_hostname' : row[1],
            'IP_address': row[2],
            'timestamp': row[3],
            'request_method': row[4],
            'path': row[5],
            'http_status_code': row[6],
            'response_time': row[7],
            'client_ip': row[8],
            'request_size': row[9],
            'tls_version': row[10],
            'host': row[11]
        }
        result_list.append(dict_row)
    return result_list

def rowInRowsFor2Columns(rows):
    result_list = []
    for row in rows:
        dict_row = {
            'row1' : row[0],
            'row2' : row[1]            
        }
        result_list.append(dict_row)
    return result_list

def rowInRowsFor3Columns(rows):
    result_list = []
    for row in rows:
        dict_row = {
            'row1' : row[0],
            'row2' : row[1],
            'row3' : row[2]            
        }
        result_list.append(dict_row)
    return result_list
