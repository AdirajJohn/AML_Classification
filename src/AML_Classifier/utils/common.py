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


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def save_json(data: dict, path: Path):
    """
    Saves the provided data as a JSON file with the specified filename.
    
    Parameters:
    data (dict or list): The data to be saved as JSON.
    filename (str): The name of the file to save the data in.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"JSON data has been written to {path}")
