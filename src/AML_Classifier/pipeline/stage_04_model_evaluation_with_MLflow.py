#pipeline
from AML_Classifier.config.configuration import ConfigurationManager
from AML_Classifier.components.model_evaluation_with_MLflow import Evaluation
from AML_Classifier import logger


STAGE_NAME="Model Evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            eval_config=config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.eval()

        except Exception as e:
            raise e
        


if __name__=="main":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< \n x===================x")
    
    except Exception as e:
        logger.exception(e)
        raise e 