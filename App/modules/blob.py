from azure.storage.blob import BlobServiceClient

#Connect to Azure Blob
connection_string = 'DefaultEndpointsProtocol=https;AccountName=storageaccpp2;AccountKey=cf7EHzObLs+CFVVVL7xJhcsEdu0Domd4DTNoipAgl7P8N1GSL6v0rOiAW7+81hSeNZk74NmmmcrX+AStmUjMDQ==;EndpointSuffix=core.windows.net'        
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = 'storagecont'
