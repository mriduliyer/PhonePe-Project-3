from azure.storage.blob import BlobServiceClient

#Connect to Azure Blob
connection_string = 'DefaultEndpointsProtocol=https;AccountName=storageaccpp2;AccountKey=clypY4aUF/1XPI4DqKnmrqv9mNkv+n9TIQxy9Q0j9YxRpK0TP0Y++AjhPuBC53N/Jh9tp4PWh6EZ+AStgfO8DQ==;EndpointSuffix=core.windows.net'        
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = 'storagecont'
