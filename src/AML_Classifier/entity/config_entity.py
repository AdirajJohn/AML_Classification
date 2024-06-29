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


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    data_dir: Path
    base_model_path: Path
    params_n_estimators: list
    params_max_depth: list
    params_min_sample_split: list
    params_min_sample_leaf: list
    params_max_features: list
    params_class_weight: str