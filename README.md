# FASTA Sequence Analysis Tool

## Overview

This project is a Python-based bioinformatics utility designed to analyze biological sequences stored in **FASTA format**. The tool parses one or more sequences from a FASTA file, computes nucleotide statistics, validates sequence content, and generates both numerical and visual summaries of the dataset.

The program is designed as a **learning-oriented bioinformatics pipeline component**, demonstrating how sequence data can be processed programmatically without relying on external libraries such as Biopython.

---

# Features

### 1. FASTA Parsing

* Reads FASTA files containing **single or multiple sequences**
* Handles multiline sequences
* Automatically separates sequences based on header lines (`>`)

---

### 2. Per-Sequence Statistics

For each sequence, the program calculates:

* Sequence ID
* Sequence length
* GC percentage
* AT percentage
* N percentage (unknown bases)

Example output:

```
ID: seq1
Length: 1200
GC%: 47.32
AT%: 51.60
N%: 1.08
```

---

### 3. Dataset Summary Statistics

The program also computes global statistics across the entire FASTA file.

Metrics include:

* Total number of sequences
* Total number of bases
* Minimum sequence length
* Maximum sequence length
* Average sequence length
* Median sequence length

Example:

```
DATASET SUMMARY
----------------
Total sequences: 50
Total bases: 120540
Min length: 320
Max length: 4980
Average length: 2410
Median length: 2385
```

---

### 4. Base Composition Analysis

The tool calculates total nucleotide composition for the dataset.

```
BASE COMPOSITION
----------------
A: 30000
T: 29000
G: 31000
C: 30500
N: 200
```

This information can reveal genome composition biases.

---

### 5. Sequence Validation

The program checks for invalid nucleotide characters.

Allowed bases:

```
A T G C N
```

If other characters appear, a warning is displayed:

```
Warning: invalid characters {'X'} in seq3
```

This helps detect corrupted or improperly formatted FASTA files.

---

### 6. CSV Export

All per-sequence statistics are exported to a CSV file for further analysis.

Output file:

```
fasta_results.csv
```

Example structure:

```
id,length,gc_percent,at_percent,n_percent
seq1,1200,47.32,51.60,1.08
seq2,850,39.15,58.50,2.35
```

This file can be used in:

* Excel
* R
* Python pandas
* statistical analysis tools

---

### 7. Data Visualization

The tool generates two plots using **matplotlib**:

1. **Sequence Length Distribution**

   Histogram showing how sequence sizes are distributed.

2. **GC Content Distribution**

   Histogram showing GC percentage variation among sequences.

These plots provide quick insights into dataset characteristics.

---

# Requirements

Python version:

```
Python 3.8+
```

Required libraries:

```
matplotlib
```

Install dependencies:

```
pip install matplotlib
```

---

# How to Run the Program

Run the script from the terminal:

```
python fasta_tool.py
```

Then enter the FASTA filename when prompted:

```
Enter FASTA filename: genome.fasta
```

---

# Example FASTA Input

```
>seq1
ATGCTAGCTAGCTAG
GCTAGCTAGCTAGC

>seq2
GGGCCCATAATAT
```

---

# Project Structure

```
fasta_analysis_tool/
│
├── fasta_tool.py
├── fasta_results.csv
├── error_log.jsonl
└── README.md
```

---

# Error Handling

If the input file cannot be found, the program logs the error in:

```
error_log.jsonl
```

Example entry:

```
2026-03-06T18:23:44 ERROR FileNotFoundError filename=genome.fasta
```

---

# Future Improvements

Possible enhancements include:

* Reverse complement generation
* k-mer frequency analysis
* sliding-window GC analysis
* command-line argument support (argparse)
* protein FASTA support
* integration with Biopython

---

# Educational Purpose

This project demonstrates key concepts in **bioinformatics programming**, including:

* file parsing
* sequence analysis
* statistical computation
* scientific data visualization
* pipeline-style program design

It is intended as a learning tool for students exploring **computational biology and genomics**.

---

# License

This project is open for educational and research use.
