from fastapi import FastAPI, UploadFile, File
from azure.storage.blob import BlobServiceClient
import os

app = FastAPI()

AZURE_CONN_STR = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "<REPLACE_WITH_YOUR_CONNECTION_STRING>")
BLOB_CONTAINER = "uploads"

@app.get("/")
def read_root():
    return {"message": "FastAPI running with Azure Blob upload!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONN_STR)
        container_client = blob_service_client.get_container_client(BLOB_CONTAINER)
        container_client.upload_blob(file.filename, file.file, overwrite=True)
        return {"status": "success", "filename": file.filename}
    except Exception as e:
        return {"status": "error", "detail": str(e)}