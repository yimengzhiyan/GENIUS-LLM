# ⚙️ Configuration Guide

*GENIUS-LLM* uses a centralized YAML configuration system to manage paths, models, and processing logic.

## 1. Project Structure
To ensure the automated path detection (GPS Logic) works correctly, please maintain the following structure:
```text
GENIUS-LLM/
├── config/
│   └── data_config.yaml    # Main configuration
├── data/                   # Input and processed data
|   ├── yourdata_process/
|   └── yourdata_process_output/
├── src/                    # Source code
├── scripts/                # main Scripts
├── requirements.txt
└── setup.py
```

## 2. YAML Field Explanations
Edit config/data_config.yaml to suit your research:

### Model Settings:
```yaml
api_key: Your LLM service provider key.
url: API endpoint (Default: DeepSeek).
model: Model ID (e.g., deepseek-chat, gpt-4o).
```

### Mongodb Settings:

```yaml
mongodb:
  uri: "mongodb://localhost:27017/"
  database: "arabidopsis_gene_db" # Database names for corresponding species (need to be changed)
```

### Data Paths(process_data):
You can define multiple data sources here. The type determines which Processor (Blast/TWAS) is used.
```yaml
data_paths:
  blast:
    input: "data/yourdata_process/01gene_blast.txt"
    output: "data/yourdata_process_output/blast_results_text.txt"
  coexpression:
    input: "data/yourdata_process/02cultivar"
    output: "data/yourdata_process_output/coexpression_output.txt"
```
### Data Paths(import_data):
```yaml
data_imports:
  blast:
    input_path: "data/yourdata_process_output/blast_results_text.txt"  # Read the gene alignment data from the file "data/test_import/01gene_blast_cleaned.txt" and import it into the MongoDB collection.
    collection: "gene_blast_similarity"
  coexpression:
    input_path: "data/yourdata_process_output/coexpression_output.txt"
    collection: "gene_coexpression"
```
## Data Format Requirements

Please ensure that all input data files strictly adhere to the following format requirements to ensure successful processing and database ingestion:

| Data Category | Supported File Formats | Description |
| :--- | :--- | :--- |
| **BLAST** | `.csv`, `.txt` | Sequence similarity and alignment results. |
| **Tissue (Expression)** | `.csv`, `.txt` | Tissue-specific gene expression profiles (e.g., TPM). |
| **KEGG** | `.csv`, `.txt` | Pathway enrichment and functional descriptions. |
| **GO** | `.csv`, `.txt` | Gene Ontology terms and functional annotations. |
| **Multi-gene Data** | `.xlsx` | Homologous gene mapping and multi-gene datasets. |
| **TWAS** | `.xlsx` | Transcriptome-Wide Association Study results. |

> **⚠️ Important**: 
> * For **CSV/TXT** files, ensure consistent delimiters (comma or tab) are used. 
> * For **XLSX** files, ensure the data is located in the first sheet unless otherwise specified in the configuration.