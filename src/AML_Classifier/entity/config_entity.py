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
    aws_access_key_id: str
    aws_secret_access_key: str

@dataclass(frozen=True)# To ensure that we give correct type of input as specified for the data ingestion process.
class dataprocessingconfig:
    root_dir: Path
    drop_feature: list
    categorical_feature: list
    continuous_feature: list
    save_processed_data: Path
    save_label_encoder: Path
    save_scaler_obj: Path
    downloaded_data: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    data_dir: Path
    base_model_path: Path
    params_n_estimators: int
    params_max_depth: int
    params_min_sample_split: int
    params_min_sample_leaf: int
    params_max_features: str
    params_class_weight: str
    

@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_url: str