import pandas as pd
import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) 

from utils.common_functions import save_to_format

## Import ./icd/who/icd102019syst_codes.txt file as pandas df
file_path = 'inputs/icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(file_path, sep=';', header=None, names=columns)

# Define columns to keep
columns_to_keep = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code']
df_small = df[['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code']].copy()
df_small = df[df_small.columns]

# Drop duplicates and count before and after cleaning
before = len(df) # Count number of rows before dropping duplicates
df = df.drop_duplicates(subset=['code'])
after = len(df) # Count number of rows after dropping duplicates

# Add a last_updated column
df_small.loc[:, "last_updated"] = "2019-10-01"

print(df_small.head())

# Creating Output directory
output_path = 'outputs/icd102019syst_codes.csv'
df.to_csv(output_path, index=False)

# Output directory with Common Functions
save_to_format(df_small, baseFile="icd102019syst_codes")

print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"Saved to {output_path}")
print(f"\nFirst 5 rows:")
print(df.head())
