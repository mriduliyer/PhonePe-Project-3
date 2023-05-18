from azure.storage.blob import BlobServiceClient

#Connect to Azure Blob
connection_string = 'DefaultEndpointsProtocol=https;AccountName=storageaccpp2;AccountKey=ZaJWUIzDJ727SiAX01jki/6T5nqGBP60PwkdQ+74Nasyh2+EqW0fhEdrwHxX75lh3I8WLA5A93Xy+ASt7puTiA==;EndpointSuffix=core.windows.net'        
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = 'storagecont'

