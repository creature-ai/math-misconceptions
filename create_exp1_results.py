import pandas as pd

output_file_path = 'outputs/experiment_1_gpt-4-turbo_2iters.csv'
outputs_df = pd.read_csv(output_file_path)

print(outputs_df.head())

# precision per MAE
precision_per_MAE = outputs_df.groupby('Misconception ID')['Correct'].mean()
precision_per_topic = outputs_df.groupby('Topic')['Correct'].mean()

print(precision_per_MAE)
print(precision_per_topic)