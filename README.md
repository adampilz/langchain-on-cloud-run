# Langchain + Cloud Run + Certex AI LLMs

Boilerplate for deploying LangChain on Digitalocean App Platform

## Deploying to Google Cloud Run, requires CloudSDK and Google Cloud Project with billing enabled

1. Use Google builds command to create the docker image in the container registry

   ```sh
   gcloud builds submit --tag gcr.io/PROJECT_ID/langchain
   ```

1. Create a Cloud Run service

   ```sh
   gcloud run deploy --image gcr.io/PROJECT_ID/langchain --timeout=300 --platform managed
   ```

1. Verify the deployed cloud run service in the Google Cloud Console
