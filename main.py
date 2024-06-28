from AML_Classifier import logger
from AML_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< \n x=========================================x")
    
except Exception as e:
    logger.exception(e)
    raise e     


STAGE_NAME="Data_Preprocessing"

try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
    data_preprocess = DataProcessingPipeline()
    data_preprocess.main()
    logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<< \n\n X=================X")
    
except Exception as e:
    logger.exception(e)
    raise e