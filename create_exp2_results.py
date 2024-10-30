import pandas as pd

output_file_path = 'outputs/experiment_2_gpt-4-turbo_100iters.csv'
outputs_df = pd.read_csv(output_file_path)

print(outputs_df.head())



def calculate_precision_recall(df):
    # Calculate precision and recall
    true_positives = df['Correct'].sum()
    total_predicted = len(df)
    total_actual = df['Misconception ID'].nunique()
    
    precision = true_positives / total_predicted if total_predicted else 0
    recall = true_positives / total_actual if total_actual else 0
    
    return precision, recall

# Overall precision and recall
overall_precision, overall_recall = calculate_precision_recall(outputs_df)

# Precision and recall per topic
topic_precision_recall = outputs_df.groupby('Topic').apply(calculate_precision_recall).apply(pd.Series)
topic_precision_recall.columns = ['Precision', 'Recall']

# Display results
print(f"Overall Precision: {overall_precision:.3f}")
print(f"Overall Recall: {overall_recall:.3f}")
print("\nPrecision and Recall per Topic:")
print(topic_precision_recall)