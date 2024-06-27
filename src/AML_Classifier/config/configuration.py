#Configration Manger

from AML_Classifier.constants.__init__ import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from AML_Classifier.utils.common import read_yaml, create_directories

from AML_Classifier.entity.config_entity import DataIngestionConfig

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