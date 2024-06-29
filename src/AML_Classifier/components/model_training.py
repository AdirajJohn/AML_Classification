from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn import metrics
from AML_Classifier.entity.config_entity import PrepareBaseModelConfig
from AML_Classifier import logger
import os
import pickle
import pandas as pd
import numpy as np
from pathlib import Path

class PrepareBaseModel:
    def __init__(self,config: PrepareBaseModelConfig):
        self.config = config

    def load_model_data(self):
        #Need to make this data ingestion dynamic
        data=pd.read_csv(Path(self.config.data_dir))
        y=data[["is_laundering"]]
        x=data.drop(["is_laundering"],axis=1)
        y=np.array(y)
        y=y.ravel()

        # Split data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        # Define the parameter grid
        param_grid = {
            'n_estimators': self.config.params_n_estimators,
            'max_depth': self.config.params_max_depth,
            'min_samples_split': self.config.params_min_sample_split,
            'min_samples_leaf': self.config.params_min_sample_leaf,
            'max_features': self.config.params_max_features
            }
        
        # Initialize the classifier
        model = RandomForestClassifier(**param_grid)

        #Train the model
        model.fit(X_train,y_train)

        #Save the ML model
        with open(self.config.base_model_path,"wb") as file:
            pickle.dump(model, file)

        
        # Prediction Value
        y_pred=model.predict(X_test)
        #eval accuracy
        accuracy=metrics.accuracy_score(y_pred,y_test)
        print("Test Set Accuracy:", accuracy)
        logger.info(f"Test accuray: {accuracy}")
   