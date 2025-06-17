# Lab 11: Working with the String Sequence and Molecular Weight of Insulin

In this lab, you'll bring together your knowledge of **string manipulation**, **variables**, and **basic Python math** to calculate the **molecular weight of human insulin**.

Using the actual amino acid sequence of insulin, you'll:
- Store segments of the protein as variables
- Combine those segments into a full insulin molecule
- Count each amino acid type
- Multiply by their known molecular weights
- Compare your calculated result to the real-world molecular weight of insulin

---

## What You'll Learn

- How to store and combine **protein sequences** as strings  
- How to count characters (amino acids) in a string  
- How to map and multiply values using **dictionaries**  
- How to calculate the **molecular weight** of a biological molecule  
- How to compute **error percentage** and compare with known values

---

## Amino Acid Chain Segments

| Segment   | Variable     | Description                         |
|-----------|--------------|-------------------------------------|
| Signal    | `lsInsulin`  | Amino acids 1–24                    |
| B-Chain   | `bInsulin`   | Amino acids 25–54                   |
| C-Chain   | `cInsulin`   | Amino acids 55–89 (non-functional)  |
| A-Chain   | `aInsulin`   | Amino acids 90–110                  |
| Insulin   | `insulin`    | Concatenation of B-Chain + A-Chain |

---

## Key Concepts in Action

- `str.count()` is used to count each amino acid in the sequence
- `aaWeights` is a dictionary containing the average molecular weight of each amino acid
- A **dictionary comprehension** is used to calculate weighted totals
- The **error percentage** compares your result to the actual molecular weight of insulin (5807.63 Da)

---

### Sample Output
The sequence of human preproinsulin:
mrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr...

The sequence of human insulin, chain a: giveqcctsicslyqlenycn

The rough molecular weight of insulin: 6696.42
Error percentage: 15.30%

---
### Why the Error Happens

Even though your calculation is based on the variable  
`insulit = bInsulin + aInsulin`  

...which is correct, your result is 6696.42 Da, while the actual molecular weight of insulin is 5807.63 Da.

This ~15.3% error happens because:

Your sequence uses one-letter amino acid codes, but the weight calculation does not account for water loss during peptide bond formation.

The molecular weight of a protein is slightly less than the sum of its free amino acids due to the release of water molecules (H₂O) when peptide bonds form.