import pandas as pd
import logging
from pathlib import Path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) 

from utils.common_functions import save_to_format

# Load path to the ICD-10-CM text file
load_icd10cm_data_filepath = "inputs/icd10cm_order_2025.txt"

# Starting to clean the raw data by adding fixed width and column names
colspecs = [(0, 6), (6, 14), (14, 16), (16, None)]
col_names = ["seq", "code", "flag", "description"]

# Checking the data
df = pd.read_fwf(load_icd10cm_data_filepath, colspecs=colspecs, names=col_names)
print(df.head())

# Set up logging -> Why Logging? It helps track what happened, when it happened, and why it happened.
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s") 
    # Set logging level to INFO, %(levelname)s - %(message)s means log level and message. 
    ## Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    ### Message: The actual log message
logging.info("ICD-10-CM processing completed successfully.")
logging.info(f"Raw data shape: {df.shape}")

# Strip spaces & uppercase
df['code'] = df['code'].str.strip().str.upper()
logging.info("Stripped and uppercased 'code' column.")
        
# Strip & Title-Case descriptions
df['description'] = df['description'].str.strip().str.title()
logging.info("Stripped and title-cased 'description' column.")
        
# Drop duplicates and count before and after cleaning
before = len(df) # Count number of rows before dropping duplicates
df = df.drop_duplicates(subset=['code'])
after = len(df) # Count number of rows after dropping duplicates
logging.info(f"Dropped {before - after} duplicate rows. Final rows: {after}")

# Preview data after cleaning
print(df.head())

# Renaming dataframe
icd10cm = df.copy()
print(icd10cm.head())

# Add a last_updated column
icd10cm ['last_updated'] = "2025-09-10"

## save as csv to medicalcodexes/outputs
output_path = "outputs/icd10cm.csv"
icd10cm.to_csv(output_path, index=False)

## save as csv to medicalcodexes/output
save_to_format(icd10cm, baseFile="icd10cm_order2025")


