from train_pipeline import data_spliter, trained_model, save_model
from utils import data_loader, yaml_loader, directory_path, yaml_writer
from datetime import datetime
import os
import numpy as np
import argparse
import mlflow 

mlflow.set_experiment('Care_home_Model')

def main(config_file:str, processed_data:str): 

    
    config_file = yaml_loader('config.yaml')
    data = data_loader(f'{config_file['processed']}/clean_data.csv')

    x_train, _, y_train, _ = data_spliter(data=data, features=config_file['features'], \
                                          target=config_file['target'], test_size=config_file['test_size'],\
                                            random_state=config_file['random_size'])
    model = trained_model(x_train=x_train, y_train=y_train)

    # mymodel = save_model(model=model, file_dir=f'{directory_path(config_file['model'])}/model.pkl')
    with mlflow.start_run() as run:
        # my_path = 'model'
        # save_path = os.path.join(os.getcwd(), "model")
        mlflow_config = yaml_loader('mlflow_config.yaml')
        # mlflow.sklearn.save_model(model, save_path)
        # mlflow.sklearn.log_model(model, 'model')
        input_example = np.array([[93, 0, 1, 8, 0, 1, 0, 1, 0, 0, 0, 1, 0]])
        mlflow.sklearn.log_model(model, 'model', input_example=input_example)        
        run_id = run.info.run_id
        timestamp = datetime.now().isoformat()

        runs_data = {
            'run_id':run_id,
            'timestamp' : timestamp
        }

        mlflow_config['runs'].append(runs_data)

        yaml_writer('mlflow_config.yaml', mlflow_config)

        mlflow.end_run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Model preparation')

    parser.add_argument('--config_file', 
                        type=str, 
                        help='Contains Configuration Parameters', 
                        default='config.yaml')
    
    parser.add_argument('--process_data', 
                        type= str, 
                        help= 'Clean dataset', 
                        default='data/processed/cleaned_data.csv')
    
    args = parser.parse_args()
    main(config_file=args.config_file, processed_data=args.process_data)