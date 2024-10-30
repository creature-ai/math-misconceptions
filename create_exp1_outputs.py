import openai
import pandas as pd
import pandas as pd
import json
import urllib
import math
import time
import random
import re
from tqdm import tqdm
from io import StringIO
import exp_lib

def experiment_1_trial(data_df, model_name):
  x = data_df.sample(frac=1)
  train_df = x.drop_duplicates('Misconception ID')
  test_df = x.iloc[::-1].drop_duplicates('Misconception ID')
  test_df = test_df.reset_index()
  prompt = exp_lib.generate_prompt_test_batch(train_df.to_dict(orient='records'), test_df.to_dict(orient='records'))
  response = exp_lib.get_gpt4_diagnosis(model_name, prompt)
  response_df = pd.read_csv(StringIO(response), header=None, names=["test_example", "diagnosis"])
  test_df["Predicted Diagnosis"] = response_df["diagnosis"].str.strip()
  test_df["Model"] = model_name
  return test_df[['Misconception ID', 'Example Number', 'Topic', 'Predicted Diagnosis', 'Model']]


def experiment_1(input_file_path, model_name, num_iterations, output_file_path):
  data_df = pd.read_json(input_file_path)
  experiment_1_results_list = []
  for i in tqdm(range(num_iterations)):
    try:
      trial_result = experiment_1_trial(data_df, model_name)
      trial_result['Trial'] = i 
      experiment_1_results_list.append(trial_result)
    except Exception as e:
      print(e)  
  experiment_1_results_df = pd.concat(experiment_1_results_list)
  experiment_1_results_df['Correct'] = (experiment_1_results_df['Misconception ID'] == experiment_1_results_df['Predicted Diagnosis'])
  experiment_1_results_df.to_csv(output_file_path)


if __name__ == '__main__':
  experiment_name = 'experiment_1'
  input_file_path = 'data/data.json' 
  model_name = 'gpt-4-turbo'
  num_iterations = 100
  output_file_path = f'outputs/{experiment_name}_{model_name}_{num_iterations}iters.csv'

  experiment_1(
    input_file_path,
    model_name,
    num_iterations,
    output_file_path
  )

