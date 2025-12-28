# Document to Structured Data Pipeline

## Overview
This project converts unstructured PDF documents into clean, structured, machine-readable data.  
It demonstrates a practical data engineering workflow including PDF ingestion, table extraction, data cleaning, and structured output generation.

The pipeline is designed to handle real-world documents (messy tables, inconsistent formatting) and transform them into reliable datasets suitable for analytics, automation, or downstream AI applications.

---

## Key Features
- PDF ingestion and processing
- Automatic table extraction from PDFs
- Data cleaning and normalization
- Structured output in CSV / JSON format
- Modular, script-based architecture
- Error handling for inconsistent data formats

---

## Tech Stack
- **Python 3**
- **Pandas** – data cleaning and transformation
- **Tabula-py** – PDF table extraction
- **Java (Tabula dependency)**
- **VS Code / Terminal**
- **Git & GitHub**

---

## Project Structure

document-to-structured-data/

│
├── data/

│   ├── raw/            # Original PDF files

│   ├── extracted/      # Extracted tables (CSV)

│   └── cleaned/        # Cleaned, structured datasets

│
├── src/

│   ├── extract_tables.py   # Extract tables from PDF

│   ├── clean_data.py       # Clean and normalize extracted data

│   └── utils.py            # Helper functions

│
├── README.md
└── requirements.txt

## Workflow
1. **Add PDF**
   - Place input PDF files inside the `data/raw/` directory.

2. **Extract Tables**
   ```bash
   python src/extract_tables.py
  • Extracts all detectable tables from the PDF.
  
	•	Saves raw tables as CSV files.
  Output
  
	•	Clean, structured CSV/JSON files ready for analysis or automation.

# Example Use Cases
	•	Converting financial or survey PDFs into datasets
	•	Preparing documents for analytics dashboards
	•	Feeding structured data into AI/ML pipelines
	•	Automating manual data extraction workflows

# Challenges Solved
	•	Handling inconsistent table structures
	•	Managing malformed CSV rows
	•	Designing a reusable, modular pipeline
	•	Working with real-world, non-clean data sources

# Future Enhancements
	•	Add NLP-based document summarization
	•	Integrate OCR for scanned PDFs
	•	Add API endpoint for document upload
	•	Automate pipeline execution
	•	Improve table detection accuracy


Author

Muhammad Hamza
🔗 LinkedIn￼
📂 GitHub￼
