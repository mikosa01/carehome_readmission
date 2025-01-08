from flask import Flask, request, url_for, render_template, redirect
import pandas as pd 
import pickle 
from  datetime import datetime
import yaml
import mlflow
from flask_cors import CORS

import os

port = int(os.environ.get('PORT', 5000))

mlflow.set_tracking_uri('../classification/mlruns')
app = Flask(__name__)
CORS(app)

with open('../classification/mlflow_config.yaml', 'r') as file:
    yam_file= yaml.safe_load(file)

df= sorted(yam_file['runs'], key= lambda x: x['timestamp'], reverse= True)
run_id = df[0]['run_id']
artifact = 'model'

model = mlflow.sklearn.load_model(f'runs:/{run_id}/{artifact}')


# model = mlflow.sklearn.load_model(artifact)

@app.route('/')
def use_template():
    return render_template('index.html')

@app.route('/predict', methods = ['POST', "GET"])
def predict():
    input_one = request.form['1']
    input_two = request.form['2']
    input_three = request.form['3']
    input_four = request.form['4']
    input_five = request.form['5']
    input_six = request.form['6']
    input_seven = request.form['7']
    input_eight = request.form['8']
    input_nine = request.form['9']
    input_ten = request.form['10']
    input_eleven = request.form['11']
    input_twelve = request.form['12']
    input_thirteen = request.form['13']

    input_values = [input_one, input_two, input_three, input_four, input_five, input_six, 
      input_seven, input_eight, input_nine, input_ten, input_eleven, input_twelve, 
      input_thirteen]
    X_val = pd.DataFrame([pd.Series([input_values])],
                            columns=["gender", "mental_health_issues", "polypharmacy", "nutritional_status", 
                                    "follow_up_completed", "care_plan_adherence", "staffing_level", 
                                    "family_involvement", "hospital_acquired_infections", 
                                    "discharge_timing", "chronic_conditions", "previous_hospitalizations", "age"]
                        )

    date = datetime.now().strftime('%Y-%m-%d')
    y_val = model.predict(X_val)[0]
    new_val = pd.DataFrame([[input_one, input_two, input_three, input_four, input_five, input_six, 
                            input_seven, input_eight, input_nine, input_ten, input_eleven, input_twelve, 
                            input_thirteen, y_val, date]], columns=["gender", "mental_health_issues", "polypharmacy", 
                                "nutritional_status",  "follow_up_completed", "care_plan_adherence", "staffing_level", 
                                "family_involvement", "hospital_acquired_infections", "discharge_timing", "chronic_conditions", 
                                "previous_hospitalizations", "age", 'readmitted_within_30_days', 'admission_date'])

    clean_data = pd.read_csv(f'../classification/data/processed/clean_data.csv')
    clean_data.reset_index(drop=True, inplace=True)
    new_val.reset_index(drop=True, inplace=True)
    update_data = pd.concat([clean_data,new_val], axis = 0, ignore_index=True)
    update_data.to_csv(f'../classification/data/processed/clean_data.csv', index=False)

    readmission_pred = model.predict_proba(X_val)
    output = '{0:.{1}f}'.format(readmission_pred[0][1], 2)
    output = str(float(output) * 100) + '%'
    if output > str(0.5):
        return render_template('result.html', pred=f'The resident would be readmitted soon enough. There is about {output} chances \
                               of the resident not to be readmitted')
    else:
        return render_template('result.html', pred=f'The resident would not be readmitted anytime soon. There is about {output} chances \
                               for then resident not to be readmitted')

if __name__== '__main__':
    app.run(host='0.0.0.0', port=port,  debug=False)