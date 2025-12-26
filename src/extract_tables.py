import tabula
import os

pdf_path = os.path.join("data", "raw", "sample.pdf")

tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

print(f"Found {len(tables)} tables")

os.makedirs("data/processed", exist_ok=True)

for i, table in enumerate(tables):
    output_path = f"data/processed/table_{i+1}.csv"
    table.to_csv(output_path, index=False)
    print(f"Saved {output_path}")
