import pandas as pd
import os
from pathlib import Path
from sklearn.preprocessing import LabelEncoder, StandardScaler
from AML_Classifier.entity.config_entity import dataprocessingconfig



class Processdata:
    def __init__(self,config: dataprocessingconfig):
        self.config = config

    def preprocessing(self):
        df=pd.read_csv(self.config.downloaded_data)
        #Drop the unnessary feature
        df=df.drop(self.config.drop_feature,axis=1)
        #Intialize a dataframe
        processed_df=pd.DataFrame()
        #Label encoding
        label_encoder = LabelEncoder()
        for i in list(self.config.categorical_feature):
            processed_df[i]=label_encoder.fit_transform(df[i])

        #Scaling the continous variable
        standard_scaler = StandardScaler()
        for i in list(self.config.continuous_feature):
            processed_df[i]=standard_scaler.fit_transform(df[[i]])

        #Save the file
        processed_df.to_csv(str(self.config.save_processed_data),index=False)