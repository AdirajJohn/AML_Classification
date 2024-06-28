from AML_Classifier.config.configuration import ConfigurationManager
from AML_Classifier.components.data_processing import Processdata
from AML_Classifier import logger

STAGE_NAME="Data Preprocessing"

class DataProcessingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        get_data_process_config = config.get_data_process_config()
        Process_data = Processdata(config = get_data_process_config)
        Process_data.preprocessing()


if __name__=='__main__':
    try:
        logger.info(f"**********************")
        logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj=DataProcessingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n X=================X")
    
    except Exception as e:
        logger.exception(e)
        raise e