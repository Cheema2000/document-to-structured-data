import pandas as pd
import os

INPUT_DIR = "data/processed"
OUTPUT_DIR = "data/cleaned"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_dataframe(df):
    # Standardize column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^a-z0-9_]", "", regex=True)
    )

    # Replace empty strings with NaN
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # Drop fully empty rows
    df = df.dropna(how="all")

    # Attempt to clean numeric columns
    for col in df.columns:
        if "amount" in col or "total" in col or "price" in col:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "")
                .astype(float, errors="ignore")
            )

    return df


for file in os.listdir(INPUT_DIR):
    if file.endswith(".csv"):
        path = os.path.join(INPUT_DIR, file)

        try:
            df = pd.read_csv(
                path,
                engine="python",
                on_bad_lines="skip"
            )
        except Exception as e:
            print(f"Failed to read {file}: {e}")
            continue

        cleaned_df = clean_dataframe(df)

        output_path = os.path.join(OUTPUT_DIR, file)
        cleaned_df.to_csv(output_path, index=False)

        print(f"Cleaned and saved: {output_path}")
