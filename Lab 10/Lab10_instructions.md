# Exercise 2: Obtaining the protein sequence of human insulin

Insulin is obtained from preproinsulin through a series of cut-and-paste procedures. Preproinsulin contains a 24aa signal sequence and an 86aa proinsulin molecule. Amino acids 25–54 and amino acids 90–110 are the processed insulin molecule. Use Python, Bash, or manual manipulation to retrieve only those amino acids in the sequence that compose insulin.

Manually or programmatically delete ORIGIN, 1, 61, //, and the spaces and return carriages.

In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as preproinsulin-seq-clean.txt.

In the file preproinsulin-seq-clean.txt, copy your results.

Confirm that your file has 110 characters of lowercase letters, which represent the amino acids in the sequence of human preproinsulin.

In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as lsinsulin-seq-clean.txt.

In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.

In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as binsulin-seq-clean.txt.

In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.

In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as cinsulin-seq-clean.txt.

In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.

In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as ainsulin-seq-clean.txt.

In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.


### Insulin Sequence Variables

| Variable Name | String to Save to Variable                  |
|---------------|---------------------------------------------|
| `lsInsulin`   | `"malwmrllpllallalwgpdpaaa"`                |
| `bInsulin`    | `"fvnqhlcgshlvealylvcgergffytpkt"`          |
| `aInsulin`    | `"giveqcctsicslyqlenycn"`                   |
| `cInsulin`    | `"rreaedlqvgqvelgggpgagslqplalegslqkr"`     |
