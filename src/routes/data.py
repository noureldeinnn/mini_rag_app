from fastapi import FastAPI,APIRouter, Depends, UploadFile
import os
from  helpers.config import Settings,get_settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload(project_id: str,file: UploadFile, app_settings: Settings = Depends(get_settings)):
    is_valid = DataController().validate_uploaded_file(file=file)
    if is_valid:
        return {"message": "File uploaded successfully","filename": file.filename,"content_type": file.content_type}
    