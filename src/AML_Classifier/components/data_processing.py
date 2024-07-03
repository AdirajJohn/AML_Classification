import pandas as pd
import os
import pickle
from pathlib import Path
import numpy as np
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
        df_le=pd.DataFrame()
        le = LabelEncoder()
        for i in self.config.categorical_feature:
            num_df=np.array(df[[i]])
            df_le[i]=le.fit_transform(num_df.ravel())
            with open(f"{self.config.save_label_encoder}/le_{i}.pkl","wb") as file:
                pickle.dump(le,file)

        #Scaling the continous variable
        sc = StandardScaler()
        sc.fit(df[self.config.continuous_feature])
        df_sc=sc.transform(df[self.config.continuous_feature])
        df_sc1=pd.DataFrame(df_sc, columns=self.config.continuous_feature)

        processed_df=pd.concat([df_le,df_sc1], axis=1)

        #Save the Scaler
        with open(self.config.save_scaler_obj,"wb") as file:
            pickle.dump(sc, file)
        

        #Save the file
        processed_df.to_csv(self.config.save_processed_data,index=False)