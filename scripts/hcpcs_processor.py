import pandas as pd
import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) 

from utils.common_functions import save_to_format

# Path to the HCPCS text file
file_path = "inputs/HCPC2025_OCT_ANWEB_v3.xlsx"

# Select Column Names 
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = ["Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"]    
df = pd.read_excel(file_path, engine="openpyxl", dtype=str, names=column_names)
print("Column Names in dataset:")
print(df.columns.tolist())

# Select the columns you want to keep 
columns_to_keep = ["Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"]
hcpcs_small = df[columns_to_keep]
print(hcpcs_small.head())

# Add a last_updated column
hcpcs_small['last_updated'] = "2025-09-10"

## save as csv to Module1_MedicalCodexes/hcpcs/output
output_path = "outputs/hcpcs_small.csv"
hcpcs_small.to_csv(output_path, index=False)

save_to_format(hcpcs_small, baseFile="HCPC2025_OCT_ANWEB")