import polars as pl
from pathlib import Path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), ".."))) 

from utils.common_functions import save_to_format

# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

# Path to the RXNATOMARCHIVE.RRF file
file_path = Path('inputs/RXNATOMARCHIVE.RRF')

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
if df.columns[-1] == "":
    df = df.drop(df.columns[-1])
print(df.shape)

# Add a last_updated column
df = df.with_columns(pl.lit("2024-06-01").alias("last_updated"))

# Save as CSV to outputs
output_path = 'outputs/RXNATOMARCHIVE.csv'
df.write_csv(output_path)

# Save as CSV to output with common function
save_to_format(df, baseFile="RXNATOMARCHIVE")

print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")