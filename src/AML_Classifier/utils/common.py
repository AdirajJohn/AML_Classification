#This script will contain commonly used functions which can be accessed across the project.
import os
from box.exceptions import BoxValueError
import yaml
from AML_Classifier import logger
import json
import joblib
from ensure import ensure_annotations # It will make sure that parameter passed to the arg will be same as defined otherwise it will throw an error
from box import ConfigBox #For easy access of the values of a key eg: dict.key1 -> gives key1's value, otherwise we would have to do dict["key1"]
from pathlib import Path
from typing import Any


#1. Function to read an csv file
@ensure_annotations
def read_csv(filepath:Path,filename:str):
    import pandas as pd
    df=pd.read_csv(filepath+filename+".csv")
    return df


