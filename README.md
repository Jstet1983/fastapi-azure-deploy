# FastAPI Azure GitHub Deploy

## Setup
1. Replace `<REPLACE_WITH_YOUR_CONNECTION_STRING>` in main.py
2. Push to GitHub (main branch).
3. Go to Azure Portal > App Service > Deployment Center
4. Connect GitHub repo and set two secrets:
   - `AZURE_APP_NAME`: name of your Azure Web App
   - `AZURE_PUBLISH_PROFILE`: XML from Deployment Center > Get publish profile

## Usage
- `GET /` returns alive check
- `POST /upload` accepts file upload, stores to Azure Blob