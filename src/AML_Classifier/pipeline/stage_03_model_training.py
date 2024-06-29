#pipeline
from AML_Classifier.config.configuration import ConfigurationManager
from AML_Classifier.components.model_training import PrepareBaseModel
from AML_Classifier import logger


STAGE_NAME="Model training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config=config.get_prepare_base_model_config()
            prepare_base_model= PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.load_model_data()
        except Exception as e:
            raise e


if __name__=="main":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< \n x=========================================x")
    
    except Exception as e:
        logger.exception(e)
        raise e  