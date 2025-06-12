# Exercise 2: Obtaining the protein sequence of human insulin

Insulin is obtained from preproinsulin through a series of cut-and-paste procedures. Preproinsulin contains a 24aa signal sequence and an 86aa proinsulin molecule. Amino acids 25–54 and amino acids 90–110 are the processed insulin molecule. Use Python, Bash, or manual manipulation to retrieve only those amino acids in the sequence that compose insulin.

1. Manually or programmatically delete ORIGIN, 1, 61, //, and the spaces and return carriages.

2. In the file preproinsulin-seq-clean.txt, copy your results.

   Confirm that your file has 110 characters of lowercase letters, which represent the amino acids in the sequence of human preproinsulin.

3. In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.

4. In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.

5. In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.

6. In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.


### Insulin Sequence Variables

| Variable Name | String to Save to Variable                  |
|---------------|---------------------------------------------|
| `lsInsulin`   | `"malwmrllpllallalwgpdpaaa"`                |
| `bInsulin`    | `"fvnqhlcgshlvealylvcgergffytpkt"`          |
| `aInsulin`    | `"giveqcctsicslyqlenycn"`                   |
| `cInsulin`    | `"rreaedlqvgqvelgggpgagslqplalegslqkr"`     |
