#Configration Manger

from AML_Classifier.constants.__init__ import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from AML_Classifier.utils.common import read_yaml, create_directories
import os
from pathlib import Path

from AML_Classifier.entity.config_entity import DataIngestionConfig,dataprocessingconfig,PrepareBaseModelConfig

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
        self.config= read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])



    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        #Create file path to store the dataset
        create_directories([config.root_dir])

        data_ingestion_config= DataIngestionConfig(
            root_dir = config.root_dir,
            service = config.service,
            region = config.region,
            bucket_name = config.bucket_name,
            aws_file = config.aws_file,
            download_path = config.download_path
        )
        return data_ingestion_config
    
    
    def get_data_process_config(self) -> dataprocessingconfig:
        config = self.config.data_prepocess
        create_directories([config.root_dir])
        downloaded_data = os.path.join(self.config.data_ingestion.root_dir,"data.csv")

        data_process_config= dataprocessingconfig(
            root_dir = Path(config.root_dir),
            drop_feature=config.drop_feature,
            categorical_feature = config.categorical_feature,
            continuous_feature = config.continuous_feature,
            downloaded_data=Path(downloaded_data),
            save_processed_data=Path(config.save_processed_data)
            )
        return data_process_config
    


    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        training_data = Path(self.config.data_prepocess.save_processed_data)

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            data_dir=Path(training_data),
            params_n_estimators = self.params.n_estimators,
            params_max_depth = self.params.max_depth,
            params_min_sample_split = self.params.min_samples_split,
            params_min_sample_leaf = self.params.min_samples_leaf,
            params_max_features = self.params.max_features,
            params_class_weight = self.params.class_weight
        )

        return prepare_base_model_config