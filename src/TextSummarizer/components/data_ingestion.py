import os
import urllib.request as request
from pathlib import Path
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from TextSummarizer.entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_dir):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_dir
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_dir))}")  

        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_dir, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)