# assume we are starting with data.json 
# then we create several files per example:
# name format as {mae}_{example_num}_question|incorrect_answer|correct_answer

import pandas as pd 
from tqdm import tqdm

df = pd.read_json('data/data.json')

for i, row in tqdm(df.iterrows()):
    mae = row['Misconception ID']
    num = row['Example Number']
    correct_answer = row['Correct Answer']
    incorrect_answer = row['Incorrect Answer']
    question = row['Question'] 
    with open(f'data/txt_files/{mae}_{num}_correct_answer.txt', 'a') as file:
        file.write(correct_answer)
    with open(f'data/txt_files/{mae}_{num}_incorrect_answer.txt', 'a') as file:
        file.write(incorrect_answer)
    with open(f'data/txt_files/{mae}_{num}_question.txt', 'a') as file:
        file.write(question)                