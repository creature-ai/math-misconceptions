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

from tqdm import tqdm

# In-context learning prompt template
def generate_prompt_test_batch(train_examples, test_examples):
    prompt = (
        "You are an expert tutor on middle school math with years of experience understanding students' most common math mistakes. "
        "You have identified a set of common mistakes called Misconceptions, and you use them to diagnose student's answers to math questions. "
        "You have also developed a labeled dataset of question items, and diagnosed them with the appropriate misconception ID.\n"
        "Using the set of misconceptions and the labeled dataset, your task today is to take some items of unlabeled data and provide a diagnosis for each unlabeled item.\n\n"
        "Here is the list of misconceptions together with a brief description:\n"
    )
    # Add training examples
    for i, example in enumerate(train_examples):
        prompt += f"""
Train Example {i+1}
Question:
{example['Question']}
Answer:
{example['Incorrect Answer']}
Diagnosis: {example['Misconception ID']}
Misconception Description: {example['Misconception']}
Topic of Misconception: {example['Topic']}

"""


    prompt += """
Below are the unlabeled Test Examples. For each Test Example, provide only the most likely Misconception ID for the Test Answer from the provided list.
Don't write anything else but a sequence of lines of the format $Test_Example_Number, $Misconception_ID

"""

    for i, example in enumerate(test_examples):
        prompt += f"""
Test Example {i+1}:
Question:
{example['Question']}
Test Answer:
{example['Incorrect Answer']}

"""

    return prompt

# GPT-4 API call
def get_gpt4_diagnosis(model, prompt):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a math expert specialized in diagnosing student misconceptions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=2000,
        frequency_penalty=0.0,

    )
    return response.choices[0].message['content'].strip()
