from utils import yaml_loader, data_loader, directory_path
import pandas as pd 
import typing as t
import argparse
import mlflow

mlflow.set_experiment('Care_Features')

def categorical_imputer (df:pd.DataFrame, cat_cols:t.List[str]) -> pd.DataFrame:
    for col in cat_cols:
        modal_val = df[col].mode()[0]
        df[col] = df[col].fillna(modal_val)
    return df 

def categorical_encoder(df:pd.DataFrame, cat_cols:t.List[str]) -> pd.DataFrame:
    encoder = {}
    for col in cat_cols:
        val_counts = df[col].value_counts(normalize=True, ascending=False).items()
        encoder[col] = {category: idx for idx, (category, _) in enumerate(val_counts, 0)}
        df[col] = df[col].map(encoder[col])
    return df

def numerical_imputer(data:pd.DataFrame, num_cols:t.List[str]) -> pd.DataFrame:
    data[num_cols] = data[num_cols].fillna(data[num_cols].mean())
    return data

def distinct_imputer(data:pd.DataFrame, dis_cols:t.List[str]) -> pd.DataFrame:
    for col in dis_cols:
        modal_val = data[col].mode()[0]
        data[col] = data[col].fillna(modal_val)
    return data

def main(config_file:str, raw_data: str , processed_data: str ): 
    
    mlflow.start_run()
    yam = yaml_loader('config.yaml')
    data = data_loader(yam['raw_data'])

    mlflow.log_param('CareFeature', ',' .join(yam['columns']))

    clean_cat = categorical_imputer(data, yam['categorical_columns'])
    clean_num = numerical_imputer(clean_cat, yam['numerical_columns'])
    clean_dis = distinct_imputer(clean_num, yam['distinct_columns'])
    clean_df = categorical_encoder(clean_dis, yam['categorical_columns'])
    clean_df.to_csv(f'{directory_path(yam['processed'])}/clean_data.csv', index=False)
    mlflow.end_run()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Preprocess data for model')

    parser.add_argument('--config_file', 
                        type=str, 
                        help='Configuration file with parameters', 
                        default='config.yaml')
    parser.add_argument('--raw_dataset', 
                        type=str, 
                        help= 'Raw dataset for transformation', 
                        default= 'data/raw/data.csv')
    parser.add_argument('--preprocessed_data', 
                        type = str, 
                        help = 'Clean dataset',
                        default='data/processed/cleaned_data.csv')
    
    args = parser.parse_args()
    main(config_file=args.config_file, 
         raw_data=args.raw_dataset, 
         processed_data = args.preprocessed_data)

    

