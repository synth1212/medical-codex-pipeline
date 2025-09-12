import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), ".."))) 

from utils.common_functions import save_to_format

## Inputs/Loinc.csv
lonic = pd.read_csv('inputs/Loinc.csv')

### Info to describe 
lonic.info()

### Strings 
lonic.STATUS.value_counts()

### Print first row 
lonic.iloc[0]

#### Check potential column names that we think we want to keep: LOINC_NUM, DefinitionDescription
lonic.LOINC_NUM
lonic['LOINC_NUM']
lonic.LONG_COMMON_NAME

list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

### List of columns to keep
lonic_small = lonic[['LOINC_NUM', 'LONG_COMMON_NAME']]
lonic_small = lonic[list_cols]

lonic_small['last_updated'] = "2025-09-03"

# lonic_small = lonic_small.rename(columns={})
lonic_small = lonic_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'long_common_name'
})

# Save to output without Common Function
file_output_path = 'medical-codex-pipeline/outputs/lonic_small.csv'
lonic_small.to_csv(file_output_path)

print(f"Output saved to {file_output_path}")

# Save to Output with Common Function 
save_to_format(lonic_small, baseFile="Loinc")

