import pandas as pd
import os
import polars as pl

def save_to_format(df:pd.DataFrame, baseFile: str, outputDir: str='output') -> None:
    os.makedirs(outputDir,exist_ok=True)
    csv_path = os.path.join(outputDir, f"{baseFile}.csv")
    if isinstance(df, pl.DataFrame):
        df.write_csv(csv_path)
    elif isinstance(df, pd.DataFrame):
        df.to_csv(csv_path, index = False)
    else:
        raise TypeError("Input df must be a pandas or polars DataFrame")
    print(f"Saved to {csv_path}")

