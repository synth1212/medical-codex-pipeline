import pandas as pd
import numpy as np

from utils.common_functions import save_to_formats

# Path to the HCPCS text file
file_path = "inputs/HCPC2025_OCT_ANWEB_v3.xlsx"

# Print Column Names based on dataset
print("Column Names based on dataset:")
# Show first column of data from the dataset; Read the file into a DataFrame
df=pd.read_excel(file_path)
print(df.columns)
# Output:
Index(['HCPC', 'SEQNUM', 'RECID', 'LONG DESCRIPTION', 'SHORT DESCRIPTION',
    'PRICE1', 'PRICE2', 'PRICE3', 'PRICE4', 'MULT_PI', 'CIM1', 'CIM2',
   'CIM3', 'MCM1', 'MCM2', 'MCM3', 'STATUTE', 'LABCERT1', 'LABCERT2',
   'LABCERT3', 'LABCERT4', 'LABCERT5', 'LABCERT6', 'LABCERT7', 'LABCERT8',
   'XREF1', 'XREF2', 'XREF3', 'XREF4', 'XREF5', 'COV', 'ASC_GRP', 'ASC_DT',
   'OPPS', 'OPPS_PI', 'OPPS_DT', 'PROCNOTE', 'BETOS', 'TOS1', 'TOS2',
   'TOS3', 'TOS4', 'TOS5', 'ANEST_BU', 'ADD DT', 'ACT EFF DT', 'TERM DT',
   'ACTION CD'],
    dtype='object')

# Select the columns you want to keep 

    lonic_small = lonic[list_cols]

def load_hcpcs_to_df(file_path):
    # You may need to adjust colspecs based on actual column widths
    # Here is a simple guess based on the sample
    colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
    column_names = [
        "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
    ]    df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)
    return df

if __name__ == "__main__":
    df = load_hcpcs_to_df(file_path)
    print(df.head())
    ## save as csv to Module1_MedicalCodexes/hcpcs/output
    output_path = "Module1_MedicalCodexes/hcpcs/output/HCPC2025_OCT_ANWEB.csv"
    df.to_csv(output_path, index=False)
