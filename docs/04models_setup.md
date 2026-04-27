🛠️ Models Setup & Inference Logic
Based on the configuration defined in config.yaml, this section details the execution environment, Large Language Model (LLM) parameters, and the bioinformatic filtering criteria used for gene function inference.


##1. RAG Backend: MongoDB Indexing
The platform utilizes a Retrieval-Augmented Generation (RAG) architecture. The LLM does not rely solely on its internal training data but queries a local MongoDB instance to retrieve biologically grounded evidence.

Database: arabidopsis_gene_db (Current focus: Arabidopsis thaliana)

Storage Logic:

Blast Similarity: Stored in gene_blast_similarity.

Regulatory Networks: Co-expression weights stored in gene_coexpression.

Phenotypic Associations: TWAS results stored in gene_trait_twas.

##2. Bioinformatic Filtering Thresholds
To ensure the high-quality synthesis of multi-omics data, the system applies hard thresholds defined in the common section of the configuration before passing data to the LLM.

| Data Category | Parameter | Threshold Value | Purpose |
| :--- | :--- | :--- | :--- |
| **BLAST** | Similarity | $\ge 0.9$ | Ensures high-confidence sequence homology. |
| **BLAST** | E-value | $\le 1 \times 10^{-5}$ | Filters out random alignments. |
| **Co-expression** | Edge Weight | $\ge 0.9$ | Focuses on strong regulatory relationships. |
| **TWAS** | Z-score | $\ge 2.0$ | Identifies statistically significant trait associations. |

##3. Inference Analysis Chain
The system processes information through a structured Chain-of-Thought (CoT) approach:

A. Data Retrieval: The system extracts structured snippets from MongoDB based on the target gene query.

B. Context Construction: Retrieved data (BLAST, Expression, GO/KEGG) are converted into a natural language prompt.

C. LLM Reasoning: The model synthesizes heterogeneous evidence to form a functional hypothesis.

Logging & Output: All intermediate reasoning steps and final predictions are stored in the configured log_path (logs/) and predict_result_output_path (predict_results) for academic audit and reproducibility.