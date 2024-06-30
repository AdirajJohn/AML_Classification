from AML_Classifier import logger
from AML_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from AML_Classifier.pipeline.stage_02_data_preprocessing import  DataProcessingPipeline
from AML_Classifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from AML_Classifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< \n x=================x")
    
except Exception as e:
    logger.exception(e)
    raise e     



STAGE_NAME="Data_Preprocessing"

try:
    logger.info(f"**********************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_preprocess = DataProcessingPipeline()
    data_preprocess.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<< \n\n X=================X")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Training"

try:
    logger.info(f"**********************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n X==============X")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Model evaluation"

try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    model_eval = ModelEvaluationPipeline()
    model_eval.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< \n x===================x")
    
except Exception as e:
    logger.exception(e)
    raise e 
