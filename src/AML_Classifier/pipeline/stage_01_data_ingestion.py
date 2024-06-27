#pipeline
from AML_Classifier.config.configuration import ConfigurationManager
from AML_Classifier.components.data_ingestion import DataIngestion
from AML_Classifier import logger


STAGE_NAME="Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config= config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()


if __name__=="main":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< \n x=========================================x")
    
    except Exception as e:
        logger.exception(e)
        raise e     