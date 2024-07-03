#Configration Manger

from AML_Classifier.constants.__init__ import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from AML_Classifier.utils.common import read_yaml, create_directories
import os
import yaml
from pathlib import Path

from AML_Classifier.entity.config_entity import DataIngestionConfig,dataprocessingconfig,PrepareBaseModelConfig, EvaluationConfig

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
        self.config= read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
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
            save_processed_data=Path(config.save_processed_data),
            save_label_encoder  = Path(config.save_label_encoder),
            save_scaler_obj = Path(config.save_scaler_obj)
            )
        return data_process_config
    
    
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
            save_processed_data=Path(config.save_processed_data),
            save_label_encoder  = Path(config.save_label_encoder),
            save_scaler_obj = Path(config.save_scaler_obj)
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
    


    def get_evaluation_config(self) -> EvaluationConfig:
        config = self.config.eval_model


        eval_config = EvaluationConfig(
            path_of_model=config.path_of_model,
            training_data=config.training_data,
            mlflow_url=config.mlflow_url,
            all_params=self.params

        )
        return eval_config