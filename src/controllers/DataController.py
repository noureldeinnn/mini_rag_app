from .BaseController import BaseController
from fastapi import UploadFile
from helpers.config import Settings

class DataController(BaseController):
    def __init__(self):
        super().__init__()  
        self.size_scale = 1048576 #convert MB to Bytes

    def validate_uploaded_file(self,file:UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            raise ValueError("File type not allowed")
        if file.size > self.app_settings.FILE_MAXIMUM_SIZE * self.size_scale:
            raise ValueError("File size exceeds maximum")
        return True
