# Lab 10: Obtaining the Protein Sequence of Human Insulin

In this lab, you’ll extract and process the protein sequence for **human insulin** from a raw `preproinsulin` sequence file.

Human insulin is derived from **preproinsulin**, which contains:
- A **24 amino acid signal sequence**
- An **86 amino acid proinsulin molecule**
- The **functional insulin molecule**, which consists of:
  - Amino acids **25–54** (B-chain)
  - Amino acids **90–110** (A-chain)

You'll clean the raw file **"preproinsulin-seq-raw"** and isolate segments of the insulin sequence using Python, Bash, or manual methods.

---

## Instructions

### Step 1: Clean the Raw Sequence

Use one of the following scripts provided to clean the original sequence file:

- For Python:  
  `python clean_sequence.py`

- For Bash:  
 `./clean_sequence.sh`

 These scripts will:  
Remove ORIGIN, 1, 61, //, spaces, and carriage returns   
Output a cleaned sequence of 110 lowercase characters

### Step 2: Save the Cleaned Sequence
The cleaned result will be saved as:

preproinsulin-seq-clean.txt

Verify: It should contain exactly 110 characters (amino acids of human preproinsulin)

### Step 3: Extract and Save Insulin Segments
From the cleaned sequence, extract the following portions and save to their respective files:

| File Name                  | Amino Acids | Expected Length |
|---------------------------|-------------|-----------------|
| lsinsulin-seq-clean.txt   | 1–24        | 24 characters   |
| binsulin-seq-clean.txt    | 25–54       | 30 characters   |
| cinsulin-seq-clean.txt    | 55–89       | 35 characters   |
| ainsulin-seq-clean.txt    | 90–110      | 21 characters   |


**Insulin Sequence Variables**  
Once you’ve extracted the segments, you can assign them to variables in Python:

| Variable Name | Sequence                                      |
|---------------|-----------------------------------------------|
| lsInsulin     | `"malwmrllpllallalwgpdpaaa"`                  |
| bInsulin      | `"fvnqhlcgshlvealylvcgergffytpkt"`            |
| aInsulin      | `"giveqcctsicslyqlenycn"`                     |
| cInsulin      | `"rreaedlqvgqvelgggpgagslqplalegslqkr"`       |
