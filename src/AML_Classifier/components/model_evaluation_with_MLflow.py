from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score,log_loss
import os
import pickle
import sklearn
import dagshub
from pathlib import Path
import mlflow.sklearn
import numpy as np
import pandas as pd
from urllib.parse import urlparse
from AML_Classifier.entity.config_entity import EvaluationConfig

class Evaluation:
    def __init__(self,config: EvaluationConfig):
        self.config = config

    def eval(self):
        data=pd.read_csv(Path(self.config.training_data))

        #Create Dependent and Independent Variable
        y=data[["is_laundering"]]
        x=data.drop(["is_laundering"],axis=1)
        y=np.array(y)
        y=y.ravel()

        # Split data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)


        #Get the trained model
        with open(self.config.path_of_model,"rb") as file:
            model=pickle.load(file)

        #Generate y_pred
        y_pred=model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)

        #Score
        save_score={
            "Accuracy": accuracy_score(y_test,y_pred),
            "F1_Score": f1_score(y_test,y_pred, average="weighted"),
            "loss": log_loss(y_test,y_pred_proba)
        }

        #Save the score JSON file
        #save_json(data=save_score,path=Path("scores.json"))


        #MLflow Integration
        dagshub.init(repo_owner='adirajjohn2000', repo_name='AML_Classification', mlflow=True)
        mlflow.set_registry_uri(self.config.mlflow_url)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(save_score)
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model,"model",registered_model_name="RandomForest")
            else:
                mlflow.sklearn.log_model(model,"model")