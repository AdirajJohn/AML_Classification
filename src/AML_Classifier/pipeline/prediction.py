import pandas as pd
import numpy as np
import pickle

class PredictionPipeline:
    def __init__(self,pred_data):
        self.pred_data=pd.DataFrame([pred_data])

    def predict(self):
        #Preprocess the data
        #load the standard scaler
        with open("model/scaler_obj.pkl","rb") as file:
            sc = pickle.load(file)

        pred_data_sc=sc.transform(self.pred_data[['from_bank', 'to_bank', 'amount_received', 'amount_paid']])
        pred_data_sc=pd.DataFrame(pred_data_sc, columns=['from_bank', 'to_bank', 'amount_received', 'amount_paid'])

        #load the label encoders
        pred_data_le=pd.DataFrame()
        for i in ['receiving_currency', 'Payment_Currency', 'Payment Format']:
            with open(f"model/le_{i}.pkl","rb") as file:
                le=pickle.load(file)
            pred_data_le[i]=le.transform(np.array(self.pred_data[[i]]).ravel())

        #Concate the two scaled data
        pred_data_scaled=pd.concat([pred_data_le,pred_data_sc],axis=1)

        #Load the model
        with open("model/base_model.pkl","rb") as file:
            model = pickle.load(file)

        #predict the output
        result=model.predict(pred_data_scaled)

        #Return the result
        if result[0]==1:
            prediction="Laundering Transaction"
            return [{"Prediction": prediction}]
        else:
            prediction = "Normal Transaction"
            return [{"Prediction": prediction}]

    

