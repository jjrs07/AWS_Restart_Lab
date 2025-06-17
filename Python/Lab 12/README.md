# Lab 12: Calculating the Net Charge of Insulin Using Python

In this lab, you'll calculate the **net electric charge** of the insulin molecule at various pH levels — using Python **lists, loops, and mathematical formulas** based on amino acid chemistry.

This is a powerful example of how **biochemistry and Python** come together for real-world applications in data science, bioinformatics, and computational biology.

---

## What You'll Learn

- How to analyze amino acid sequences using string manipulation  
- How to use a **dictionary of pKa values** (`pKR`) for charge-carrying amino acids  
- How to implement the **Henderson–Hasselbalch equation** in code  
- How to calculate the **net charge of insulin** across pH levels from 0 to 13  
- How to use loops and list comprehensions for scientific computation

---

## Key Concepts in This Lab

- **Amino acids** can be positively or negatively charged depending on pH
- Each charge-carrying amino acid has a **pKa value** stored in the `pKR` dictionary
- The **net charge** at a given pH is calculated by summing:
  - The positive charges (Lysine `K`, Histidine `H`, Arginine `R`)
  - The negative charges (Tyrosine `Y`, Cysteine `C`, Aspartic Acid `D`, Glutamic Acid `E`)

---

## How It Works

- The insulin sequence is analyzed for how many of each charge-relevant amino acid it contains
- A `while` loop increments the pH from 0 to 13
- At each pH, it calculates the net charge using the Henderson–Hasselbalch equation:

Net Charge = Positive Group Charges - Negative Group Charges

## Sample Output
14.00 -0.01723639630929136


This means that at approximately **pH 14**, the net charge of the insulin molecule is close to zero — indicating a **neutral or slightly negative charge**.

---

## Why This Matters

This lab simulates how proteins behave in different environments — something critical in:
- Drug development
- pH-sensitive delivery systems
- Protein folding and solubility studies

You're using Python to do **real science**, and this kind of work mirrors what pros in biotech and pharma use every day.



