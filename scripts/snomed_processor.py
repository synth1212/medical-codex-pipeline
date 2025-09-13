import polars as pl
from pathlib import Path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), ".."))) 
from utils.common_functions import save_to_format

# Path to Raw Data 
file_path = Path('inputs/sct2_Description_Full-en_US1000124_20250301.txt')

# Read and load the raw data with delimiter of [/t] and assign column headers
df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

# Select the columns you want to keep
cols = ["term"]
snomed_small = df[cols]
print(snomed_small.head())

# Clean data by replacing the multiple spacing with just a single spacing
snomed_small["term"].str.strip_chars().str.replace_all(r"\s+", " ").alias("term")

# Keep only unique code values to eliminates potential duplicate codes
snomed_small = snomed_small.unique(subset=['term'])

# Add a last_updated column
df = df.with_columns(pl.lit("2025-09-10").alias("last_updated"))

# Save as CSV to outputs
output_path = 'outputs/sct2_Description_Full-en_US1000124_20250301.csv'
df.write_csv(output_path)

# Save as CSV to output with common function
save_to_format(df, baseFile="sct2_Description_Full-en_US1000124_20250301")

# Check the output file size 
file_path2 = "outputs/sct2_Description_Full-en_US1000124_20250301.csv"
size_bytes = os.path.getsize(file_path2)
size_mb = size_bytes / (1024 * 1024)
print(f"CSV size: {size_bytes:,} bytes ({size_mb:.2f} MB)")

# Print summary statistics
print(f"Successfully parsed {len(df)} records from SNOMED CT file")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
print(f"Language codes: {df['languageCode'].unique().to_list()}")