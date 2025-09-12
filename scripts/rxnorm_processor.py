import polars as pl
from pathlib import Path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) 

from utils.common_functions import save_to_format

# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

# Path to the RXNATOMARCHIVE.RRF file
file_path = Path('Module1_MedicalCodexes/rxnorm/files/RXNATOMARCHIVE.RRF')

# Define the column names based on RXNATOMARCHIVE.RRF structure
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

# Read the RRF file using Polars
df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

# Drop the last empty column if it exists
if df.columns[-1] == '':
    df = df.drop(df.columns[-1])

# Add a last_updated column
df = df.with_column(pl.lit("2024-06-01").alias("last_updated"))

# Save as CSV to Module1_MedicalCodexes/rxnorm/output
output_dir = Path('Module1_MedicalCodexes/rxnorm/output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE.csv'

df.write_csv(output_path)

print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")