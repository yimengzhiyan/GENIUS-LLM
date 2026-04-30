# 🚀 Quick Start Guide

This guide will walk you through the standard workflow of **GENIUS-LLM**, from downloading the source code to generating your first gene function prediction.

---
## 1. Download the Project

To install **GENIUS-LLM**, follow these steps:
From Source:
```
# 1. Clone the repository
git clone https://github.com/ZhengJieBioinformatics/GENIUS-LLM.git
cd GENIUS-LLM

# 2. Create a clean environment (Optional but highly recommended)
conda create -n genius_llm python=3.12 -y
conda activate genius_llm

# 3. Install dependencies first to avoid failures
pip install -r requirements.txt

# 4. Install GENIUS-LLM in editable mode
pip install -e .
```
Find out packages that lead to failures, then create a new requirements.txt of them and run:
```
pip install -r requirements.txt
```

## 2. Fast Configuration
Before running, you must provide your API credentials. GENIUS-LLM is designed to be provider-agnostic.

Edit config/data_config.yaml:
```Linux 
cd config/data_config.yaml
```
```
model:
    url: https://api.openai.com/v1 # Here is the base URL for the API; you can modify it according to your specific LLM configuration.
    api_key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx # Replace your api_key
    model: The model you want to use 
```
## 3. Start MongoDB

Before running any commands, the MongoDB service must be active.

Option A (Standard): 
```bash 
sudo systemctl start mongod
```
Option B (No-root/Conda):
```bash 
mongod --dbpath ./mongodb_data --port 27017 --fork --logpath ./mongodb_data/mongodb.log
```
## 4. The Three-Step Workflow
GENIUS-LLM simplifies complex bioinformatics pipelines into three standardized commands.

**If execution fails, please check whether `config/data_config.yaml` has been properly updated.


### Step 1: Pre-process Raw Data
Clean and format your input data for LLM compatibility.
```bash
genius-process 
```
**What it does**: Reads raw files (CSV/XLSX/TXT) from ```data/yourdata_process``` and converts them into structured text.

**Output**: Generated text files in ```data/yourdata_process_output/```.
If you successfully process the raw data, you will see:

??? success "View the pre-processed logs"
    ```text
    (genius_llm) [zhengjie@localhost GENIUS-LLM]$ genius-process
    Processing blast...
      Input: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process/01gene_blast.txt
    Processing BlastProcessor...
    Finished processing BlastProcessor
    ✅ blast processed successfully.
    Processing coexpression...
      Input: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process/02cultivar
    Processing CoexpressionProcessor...
    Finished processing CoexpressionProcessor
    ✅ coexpression processed successfully.
    Processing expression...
      Input: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process/03all_Tissue_mean_TPM.csv
    Processing ExpressionProcessor...
    Finished processing ExpressionProcessor
    ✅ expression processed successfully.
    Processing homolog...
      Input: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process/04multi_gene_data.xlsx
    Processing HomologProcessor...
    Finished processing HomologProcessor
    ✅ homolog processed successfully.
    Processing twas...
      Input: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process/05TWAS_out_240925.xlsx
    Processing TwasProcessor...
    Finished processing TwasProcessor
    ✅ twas processed successfully.
    Processing kegg...
      Input: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process/06KEGG.csv
    Processing KEGGProcessor...
    Finished processing KEGGProcessor
    ✅ kegg processed successfully.
    Processing go...
      Input: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process/07GO.csv
    Processing GOProcessor...
    Finished processing GOProcessor
    ✅ go processed successfully.
    ```

### Step 2: Import Knowledge Base
First, make sure your MongoDB is running.Then populate your local MongoDB with gene annotation data.
```bash
genius-import 
```

**What it does**: Connects to your local MongoDB and uploads the pre-processed data.

**Verification**: You can check the import status in the logs or via MongoDB Shell.

Method 1: Check the Console & Log Files
```bash
# View the last 20 lines of the log
tail -n 20 logs/import_data.log 
```
Method 2: Inspect via MongoDB Shell (Most Reliable)

If you successfully import the data, you will see:
This confirms the data is actually residing in the database engine. Run the following commands in your terminal:
```bash
mongosh --port 27017 #Connect to the database
```
```JavaScript
// Switch to the project database
use arabidopsis_gene_db

// List all collections to ensure they were created
show collections

// Count records in a specific collection (e.g., GO terms)
// It should return a number > 0 (e.g., 191057)
db.go_terms.countDocuments()

// Preview one document to check if the fields are correctly mapped
db.gene_expression.findOne()

// Exit the shell
exit
```

You should see something like this:
```text
arabidopsis_gene_db> db.gene_expression.findOne()
{
  _id: ObjectId('69f2cb65d35dc210de591c42'),
  gene_id: 'Ghir_A01G000010',
  tissue_expression: { anther: 0.347761 }
}
```


??? success "View the import logs"
    ```text
    (genius_llm) [zhengjie@localhost GENIUS-LLM]$ genius-import
    Starting import for blast...
      Source file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/blast_results_text.txt
    Importing data to collection: gene_blast_similarity
    Finished importing data to gene_blast_similarity
      ✅ Finished import for blast.
    Starting import for coexpression...
      Source file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/coexpression_output.txt
    Importing data to collection: gene_coexpression
    Finished importing data to gene_coexpression
      ✅ Finished import for coexpression.
    Starting import for expression...
      Source file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/expression_output.txt
    Starting to process file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/expression_output.txt
    Parsed 65608 records from /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/expression_output.txt
    Successfully imported data into collection: gene_expression
      ✅ Finished import for expression.
    Starting import for homolog...
      Source file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/homolog_output.txt
    Importing data to collection: homologous_genes
    Finished importing data to homologous_genes
      ✅ Finished import for homolog.
    Starting import for twas...
      Source file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/twas_output.txt
    Importing data to collection: gene_trait_twas
    Finished importing data to gene_trait_twas
      ✅ Finished import for twas.
    Starting import for kegg...
      Source file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/KEGG_descriptions.txt
    Starting to process KEGG file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/KEGG_descriptions.txt
    Parsed 68835 records from /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/KEGG_descriptions.txt
    Successfully imported data into collection: kegg_pathways
      ✅ Finished import for kegg.
    Starting import for go...
      Source file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/GO_descriptions.txt
    Starting to process GO file: /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/GO_descriptions.txt
    Parsed 191057 records from /home/zhengjie/test_genius/GENIUS-LLM/data/yourdata_process_output/GO_descriptions.txt
    Successfully imported data into collection: go_terms
      ✅ Finished import for go.
    ```
### Step 3: Execute Prediction
Run the intelligent prediction engine to infer gene functions.
```bash
genius-predict AT1G01010
```

**What it does**: Retrieves multi-omics data for the specific gene and calls the LLM to generate a reasoning report.

## 4. Expected Output
After running genius-predict, you should see logs indicating the progress. The final results will be saved in the directory defined in your config (default: `predict_results/`).

## 5. Sample Log Output (DeepSeek-V3 Example)
```Plaintext
(genius_llm) [zhengjie@localhost GENIUS-LLM]$ genius-predict AT1G03000

--- GENIUS-LLM Prediction System ---
2026-04-30 12:25:44,855 - INFO - Starting prediction for Gene ID: AT1G03000
2026-04-30 12:25:45,164 - INFO - Prompt successfully generated.
2026-04-30 12:25:45,763 - INFO - HTTP Request: POST https://api.deepseek.com/chat/completions "HTTP/1.1 200 OK"
2026-04-30 12:25:51,167 - INFO - Model response received.

=== Prediction Result ===
 Based on a comprehensive analysis of all available datasets for the target gene 'AT1G03000', here is a detailed prediction of its biological function.

### Final Analysis for Gene 'AT1G03000'

#### 1. Predicted Function
Due to the complete absence of data from all seven provided sources (BLAST, Co-expression, Expression, Homologous genes, TWAS, GO, and KEGG), the biological function of gene 'AT1G03000' cannot be predicted based on these datasets alone. The gene is likely either conditionally expressed (e.g., only under specific stress or developmental stages not tested in the provided data), a non-coding RNA with a regulatory function, or a currently uncharacterized locus.

#### 2. Supporting Evidence
Since no data was found in any category, there is no evidence to support a specific functional prediction.

#### 3. Potential Traits
Without any expression, TWAS, or homology data, no specific traits can be associated with gene 'AT1G03000'. The gene's influence on any trait is unknown.

#### 4. Upregulation/Downregulation Analysis
No expression data is available. Therefore, an analysis of upregulation or downregulation in specific tissues or conditions is not possible.

#### 5. Step-by-Step Reasoning
1.  **Firstly**, the highest priority data source (TWAS) provided no associations. This means there is no direct statistical link between this gene and any specific trait or phenotype in the provided datasets.
2.  **Furthermore**, the medium-high confidence data (Homologous Gene Data) and medium confidence data (Expression Data) are both empty. This failure to find conserved functions or tissue-specific activity severely limits the ability to infer a role.
3.  **Lastly**, all supporting and foundational data sources (BLAST, Co-expression, GO, and KEGG) are also unavailable. The complete absence of information across all data types prevents any meaningful functional inference. The gene remains uncharacterized within the scope of the provided datasets.
2026-04-30 12:25:51,167 - INFO - Task completed successfully.
2026-04-30 12:25:51,167 - INFO - Prediction result successfully saved to /home/zhengjie/test_genius/GENIUS-LLM/predict_results/AT1G03000_prediction.txt
```

## 6.Data Input Format Specifications

To ensure the `genius-process` script correctly parses your raw data, please prepare your files according to the required headers and formats listed below.

| Data Type | Required Headers | File Format | Example Record |
| :--- | :--- | :--- | :--- |
| **BLAST** | `query`, `subject`, `similarity`, `alignment_length`, `mismatches`, `gap_openings`, `q_start`, `q_end`, `s_start`, `s_end`, `e_value`, `bit_score` | `TXT` (Space-sep, **No Header**) | `GeneA GeneB 85.5 200 2 0 1 200 50 250 1e-50 450` |
| **Co-expression** | `row`, `col`, `weight` | `TXT` (Space-sep, With Header) | `GeneA GeneB 0.956789` |
| **Expression** | `GeneId`, `Tissue_1`, `Tissue_2`, ... | `CSV` (Comma-separated) | `GeneA, 12.5, 0.0, 8.45` |
| **GO** | `GeneID`, `GO`, `Ontology`, `Description` | `CSV` (Comma-separated) | `GeneA, GO:0008150, BP, cell growth` |
| **KEGG** | `GeneID`, `KEGG`, `KEGG_Description` | `CSV` (Comma-separated) | `GeneA, path:ath00010, Glycolysis` |
| **TWAS** | `GeneID`, `Phenotype`, `Stage`, `TWAS.Zscore` | `XLSX` (Must be **Sheet1**) | `GeneA, FE, Stage_1, 3.4567` |
| **Homolog** | `GeneID`, `Homology of AtGi`, `Symbol`, `Full_name`, `Chr.`, `Start`, `End`, `Function description` | `XLSX` | `GeneA, AT1G01010, ABC1, Protein X, Chr1, 100, 500, Kinase` |

---

### 🛠️ Processing Notes

>*   **BLAST Header Requirement**: The system reads BLAST files without a header (`header=None`). Ensure the first line of the file contains actual data.
>*   **Co-expression Threshold**: The processor only handles gene pairs with a `weight > 0.9` to ensure the reliability of functional inference.
>*   **Dynamic Expression Columns**: Except for the first column (`GeneId`), all subsequent columns are automatically identified as tissue names.
>*   **TWAS Phenotype Mapping**: The system includes a built-in mapping dictionary that automatically converts abbreviations (e.g., `FE`, `FS`, `FU`, `FL`) into full fiber trait descriptions.
>*   **Homology Data Completion**: If any column in the homology table is missing data, the system will automatically fill the field with `NA`.

