# Insulin Molecular Weight Calculator Using JSON Data

This Python program calculates the **approximate molecular weight** of human insulin by parsing sequence and molecular data from a structured `insulin.json` file.

It combines **biological knowledge** with **modular Python programming** — perfect for learners exploring bioinformatics, data parsing, or scientific computing.

---

## What You'll Learn

- How to read and parse structured biological data from a `.json` file  
- How to extract nested data for individual insulin chain segments  
- How to calculate the molecular weight based on amino acid composition  
- How to compare computed values to known molecular weights  
- How to use lists, loops, and dictionaries in real-world scientific tasks

---

## Input File: `insulin.json`

The JSON file includes:
- **Insulin chain segments**:  
  `lsInsulin` (signal), `bInsulin`, `aInsulin`, `cInsulin`  
- **Amino acid weights** (20 standard amino acids)  
- **Known molecular weight** of functional insulin for accuracy comparison

### Sample JSON (excerpt):
```json
{
  "molecules": {
    "lsInsulin": "malwmrllpllallalwgpdpaaa",
    "bInsulin": "fvnqhlcgshlvealylvcgergffytpkt",
    "aInsulin": "giveqcctsicslyqlenycn",
    "cInsulin": "rreaedlqvgqvelgggpgagslqplalegslqkr"
  },
  "weights": {
    "A": 89.09, "C": 121.16, "D": 133.10, ...
  },
  "molecularWeightInsulinActual": 5807.63
}
```
## How the Program Works
1. Imports and uses a helper module: jsonFileHandler  
2. Reads the insulin JSON file
3. Extracts:  
- bInsulin and aInsulin to form the functional insulin molecule
- Amino acid weights (weights)  
- Actual known molecular weight for comparison
4. Counts each amino acid in the sequence
5. Calculates the estimated molecular weight using a dictionary formula
6. Computes and prints the percent error from the actual value

## Sample Output

bInsulin: fvnqhlcgshlvealylvcgergffytpkt
aInsulin: giveqcctsicslyqlenycn
molecularWeightInsulinActual: 5807.63
The rough molecular weight of insulin: 5802.51
Percent error: -0.0883%


## Why This Matters
- JSON-driven design allows clean data separation from logic
- Biological sequence analysis is a core skill in bioinformatics and biotech
- You practice real-life problem-solving using dictionaries, loops, and string manipulation

