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

@dataclass(frozen=True)# To ensure that we give correct type of input as specified for the data ingestion process.
class dataprocessingconfig:
    root_dir: Path
    drop_feature: list
    categorical_feature: list
    continuous_feature: list
    save_processed_data: Path
    downloaded_data: Path