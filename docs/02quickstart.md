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

## 5. Sample Log Output (GPT-4o Example)
```Plaintext
(genius_llm) [zhengjie@localhost rice_gene_database]$ genius-predict LOC_Os01g01030

--- GENIUS-LLM Prediction System ---
2026-04-30 23:10:04,739 - INFO - Starting prediction for Gene ID: LOC_Os01g01030
2026-04-30 23:10:06,107 - INFO - Prompt successfully generated.
2026-04-30 23:10:06,847 - INFO - HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
2026-04-30 23:10:29,468 - INFO - Model response received.

=== Prediction Result ===
 Based on the provided data for the target gene 'LOC_Os01g01030', here is a detailed prediction of its biological function, associated processes, and relevant traits.

### **1. Predicted Function**
LOC_Os01g01030 is predicted to encode a copper-binding oxidoreductase enzyme involved in cell wall remodeling and cell growth, specifically tip growth. It is likely anchored to the plasma membrane (via a GPI-anchor) and plays a critical role in the development of reproductive tissues, particularly during pollen tube growth and panicle development, and also under heat stress conditions.

### **2. Supporting Evidence**

#### **Gene Ontology (GO) Data (High Confidence)**
The GO data provides the most direct evidence for the gene's function.
- **Molecular Function**: The gene is strongly associated with `GO:0016491 (oxidoreductase activity)` and `GO:0005507 (copper ion binding)`. This combination is a hallmark of a specific class of enzymes known as **cupredoxins** (e.g., laccases, ascorbate oxidases, or plantacyanins), which often function in the apoplast or cell wall.
- **Biological Process**: Crucially, the gene is associated with `GO:0009932 (cell tip growth)` and `GO:0009826 (unidimensional cell growth)`. In plants, cell tip growth is a specialized process primarily used by **pollen tubes** and root hairs.
- **Cellular Component**: The gene is localized to the `GO:0048046 (apoplast)`, `GO:0005618 (cell wall)`, `GO:0005886 (plasma membrane)`, `GO:0046658 (anchored component of plasma membrane)`, and `GO:0031225 (anchored component of membrane)`. This suggests the protein is secreted and attached to the outer leaflet of the plasma membrane via a glycosylphosphatidylinositol (GPI) anchor. This is a common location for cell wall remodeling enzymes.

#### **Gene Expression Data (Medium Confidence)**
The expression data strongly corroborates the GO-based hypothesis of a role in reproductive development and stress response.
- **High Expression in Reproductive Tissues**: The highest expression levels are observed in **'Panicles, young'** (24.73), **'Inflorescence'** (17.57), and **'Glume'** (12.89). This indicates a specific and critical role during the early stages of reproductive organ development.
- **Expression in Anthers vs. Pistils**: There is high expression in **'Anther'** (8.72) but very low expression in **'Anthers'** (0.27). This discrepancy (possibly different developmental stages) suggests a dynamic role at a specific point in anther development. Expression in **'Pistils'** (6.00) is also moderate, consistent with a role in the female reproductive tract.
- **Upregulation under Heat Stress**: Expression is significantly upregulated under **'Seedling_Heat_Stress'** (10.47) compared to the control (3.17), suggesting the gene's product may be involved in heat stress tolerance, perhaps by maintaining cell wall integrity.
- **Downregulation under Stress Conditions**: Expression is strongly downregulated under **'Seedling_Cold'** (0.53), **'Seedling_Salt_stress_24_hr'** (0.12), and **'Leaf_seedling,Cold_Stress_24_hr'** (0.54), indicating its expression is suppressed under non-heat-related abiotic stresses.

#### **Co-expression Data (Supporting Confidence)**
The co-expression partners, while not explicitly annotated here, are consistent with the predicted function. The high co-expression weight (all >0.96) with these genes suggests they are part of a tightly regulated module. For example, `LOC_Os05g51060`, `LOC_Os09g30010`, and `LOC_Os02g44890` are often associated with cell wall metabolism or stress signaling in other plants, supporting the idea that `LOC_Os01g01030` is a central component of a cell wall remodeling and stress response network.

### **3. Potential Traits**
Based on the integrated evidence, `LOC_Os01g01030` may influence the following traits:

1.  **Panicle and Grain Development**: Its exceptionally high expression in young panicles and inflorescences suggests a vital role in panicle architecture, spikelet fertility, and grain development. A defect could lead to reduced grain number or size.
2.  **Pollen Tube Growth and Fertility**: The GO term association with `cell tip growth` and expression in anthers and pistils strongly points to a role in pollen tube germination and growth. This is essential for successful fertilization. Downregulation could lead to reduced male fertility.
3.  **Heat Stress Tolerance**: Upregulation under heat stress indicates the gene's product might help rice plants cope with high temperatures, a major environmental constraint, especially during the sensitive reproductive stage.

### **4. Upregulation/Downregulation Analysis**

| Condition | Expression Level | Trend | Potential Biological Role |
| :--- | :--- | :--- | :--- |
| **Panicles, young** | 24.73 | **Strongly Upregulated** | Active involvement in early panicle and floret development. |
| **Seedling_Heat_Stress** | 10.47 | **Upregulated** (vs. Control 3.17) | Active role in heat stress response, possibly repairing or remodeling the cell wall. |
| **Infloresence** | 17.57 | **Strongly Upregulated** | Essential role in the development of the entire inflorescence. |
| **Seedling_Cold** | 0.53 | **Downregulated** (vs. Control 3.17) | Gene activity is suppressed, as cell wall remodeling for tip growth is not a priority under cold stress. |
| **Seedling_Salt_stress_24_hr** | 0.12 | **Strongly Downregulated** | Expression is shut down, likely to conserve energy under severe osmotic stress. |
| **Leaf / Stem** | 0.27 / 0.81 | **Low / Baseline** | Protein function is not needed in these tissues under standard conditions. |

### **5. Step-by-Step Reasoning**

1.  **Firstly**, the highest confidence data, the **Gene Ontology (GO)** information, provided the core hypothesis. The combination of `oxidoreductase activity`, `copper ion binding`, and `cell tip growth` is a fingerprint for a **cupredoxin-like enzyme** crucial for pollen tube growth. The `anchored component of plasma membrane` and `apoplast` localizations suggest it is a secreted, GPI-anchored protein that acts on the cell wall from the outside.

2.  **Secondly**, this hypothesis was strongly validated by the **Gene Expression Data**. The highest expression by a large margin was found in **'Panicles, young'** and **'Inflorescence'**, which are the very tissues where massive cell tip growth (pollen formation and development) and cell wall expansion are happening.

3.  **Furthermore**, the expression pattern under stress provides further nuance. Upregulation under **Heat Stress** suggests this enzyme's role in cell wall remodeling is also critical for thermotolerance. Conversely, its downregulation under cold and salt stress implies its expression is tightly regulated and specifically tied to growing tissues or heat stress, rather than a general stress protein.

4.  **Lastly**, while no BLAST or KEGG data was available, the **Co-expression Data** serves as supporting evidence. The extremely high correlation (>0.96) with ten other genes confirms that `LOC_Os01g01030` is part of a tightly co-expressed genetic module, likely dedicated to a specific process (e.g., panicle development). This reinforces that the gene is not functionally isolated but a core part of a larger biological pathway, as suggested by the GO and expression data.

**Conclusion**: The gene `LOC_Os01g01030` is a copper-binding oxidoreductase (likely a plantacyanin or laccase-like protein) anchored to the plasma membrane in the apoplast. Its primary function is to mediate cell wall remodeling during **cell tip growth in reproductive tissues** (pollen tubes, developing panicles) and is also involved in the **response to heat stress**.
2026-04-30 23:10:29,469 - INFO - Task completed successfully.
2026-04-30 23:10:29,469 - INFO - Prediction result successfully saved to /home/zhengjie/test_genius/GENIUS-LLM/predict_results/LOC_Os01g01030_prediction.txt```

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

