import json
import os
from datetime import datetime

INPUT_DIR = "data/json"
OUTPUT_DIR = "data/ai_outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_summary(content):
    columns = content.get("columns", [])
    row_count = content.get("row_count", 0)

    numeric_cols = []
    text_cols = []

    if content["data"]:
        sample = content["data"][0]
        for col, value in sample.items():
            try:
                float(value)
                numeric_cols.append(col)
            except:
                text_cols.append(col)

    summary = (
        f"This table contains {row_count} records. "
        f"It includes {len(numeric_cols)} numeric fields "
        f"({', '.join(numeric_cols[:3])}) and "
        f"{len(text_cols)} descriptive fields "
        f"({', '.join(text_cols[:3])})."
    )

    insights = []
    if numeric_cols:
        insights.append("Numeric columns may be used for aggregation and trend analysis.")
    if text_cols:
        insights.append("Text fields can be used for categorization or search.")

    return summary, insights


for file in os.listdir(INPUT_DIR):
    if file.endswith(".json"):
        path = os.path.join(INPUT_DIR, file)

        with open(path, "r") as f:
            content = json.load(f)

        summary, insights = generate_summary(content)

        output = {
            "source_file": file,
            "generated_at": datetime.utcnow().isoformat(),
            "summary": summary,
            "insights": insights
        }

        output_path = os.path.join(
            OUTPUT_DIR,
            file.replace(".json", "_summary.json")
        )

        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)

        print(f"Mock AI summary created: {output_path}")
