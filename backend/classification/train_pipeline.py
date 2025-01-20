import pandas as pd
import typing as t
import os
import joblib
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def data_spliter (data:pd.DataFrame, features: t.List[str], target:t.List[str],\
                   random_state:int , test_size:int) -> t.Union[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    x_train, x_test, y_train, y_test = train_test_split(data[features], data[target], \
                                                        random_state=random_state, test_size=test_size)
    return x_train, x_test, y_train, y_test

def trained_model (x_train:pd.DataFrame, y_train:pd.Series) -> XGBClassifier:
    model = XGBClassifier()
    model.fit(x_train, y_train)

    return model


def save_model(model:XGBClassifier, file_dir:str):
    script_dir = os.path.dirname(__file__)
    config_path= os.path.join(script_dir, file_dir)
    with open(config_path, 'wb') as mymodel:
        joblib.dump(model, mymodel)
        
