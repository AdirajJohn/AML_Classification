#Entity
from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen=True)# To ensure that we give correct type of input as specified for the data ingestion process.
class DataIngestionConfig:
    root_dir: Path
    service: str
    region: str
    bucket_name: str
    aws_file: str
    download_path: Path