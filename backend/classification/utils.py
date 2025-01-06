import pandas as pd 
import numpy as np 
import yaml
from sklearn.model_selection import train_test_split
import os 




def yaml_loader(file_dir:str ) -> dict:
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir,file_dir)
    with open (config_path, 'r') as myYaml:
        file = yaml.safe_load(myYaml)
    return file

def yaml_writer(file_dir:str, data:dict) -> None:
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir,file_dir)
    with open (config_path, 'w') as file:
        file = yaml.safe_dump(data, file, default_flow_style=False)

def data_loader(file_dir:str ) -> pd.DataFrame: 
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir,file_dir)
    data = pd.read_csv(config_path)
    return data

def directory_path(path:str) -> str:
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir,path)
    if not os.path.exists(config_path):
        os.makedirs(config_path)
    return config_path





