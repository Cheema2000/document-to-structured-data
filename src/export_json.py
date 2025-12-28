import pandas as pd
import os
import json
from datetime import datetime

INPUT_DIR = "data/cleaned"
OUTPUT_DIR = "data/json"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if file.endswith(".csv"):
        path = os.path.join(INPUT_DIR, file)
        df = pd.read_csv(path)

        payload = {
            "source_file": file,
            "generated_at": datetime.utcnow().isoformat(),
            "row_count": len(df),
            "columns": list(df.columns),
            "data": df.to_dict(orient="records")
        }

        output_path = os.path.join(
            OUTPUT_DIR,
            file.replace(".csv", ".json")
        )

        with open(output_path, "w") as f:
            json.dump(payload, f, indent=2)

        print(f"Exported JSON: {output_path}")
