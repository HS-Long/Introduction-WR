import pandas as pd
from pathlib import Path

def load_csv(file_path: str):
    csv_path = Path(file_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"{csv_path} not found.")

    encodings = ["utf-8", "cp1252", "latin1"]
    for enc in encodings:
        try:
            df = pd.read_csv(csv_path, encoding=enc)
            print(f"Loaded {file_path} using encoding: {enc}")
            return df
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("All encoding attempts failed.")
