from datetime import datetime
import json
import csv
import statistics
import matplotlib.pyplot as plt

filename = input("Enter FASTA filename: ")

valid_bases = set("ATGCN")

seq_number = 0
current_header = None

length = 0
gc_count = 0
at_count = 0
n_count = 0

# global counts
total_A = 0
total_T = 0
total_G = 0
total_C = 0
total_N = 0

all_sequences = []

try:
    with open(filename, encoding="utf-8-sig") as file:

        for line in file:

            line = line.strip().upper()

            if line == "":
                continue

            if line.startswith(">"):

                # finalize previous sequence
                if current_header is not None:

                    all_sequences.append({
                        "id": current_header,
                        "length": length,
                        "gc_percent": (gc_count/length*100) if length else 0,
                        "at_percent": (at_count/length*100) if length else 0,
                        "n_percent": (n_count/length*100) if length else 0
                    })

                seq_number += 1
                current_header = line[1:].split()[0]

                length = 0
                gc_count = 0
                at_count = 0
                n_count = 0

            else:

                # validation
                invalid = set(line) - valid_bases
                if invalid:
                    print(f"Warning: invalid characters {invalid} in {current_header}")

                length += len(line)

                gc = line.count("G") + line.count("C")
                at = line.count("A") + line.count("T")
                n = line.count("N")

                gc_count += gc
                at_count += at
                n_count += n

                total_A += line.count("A")
                total_T += line.count("T")
                total_G += line.count("G")
                total_C += line.count("C")
                total_N += n

        # store final sequence
        if current_header is not None:
            all_sequences.append({
                "id": current_header,
                "length": length,
                "gc_percent": (gc_count/length*100) if length else 0,
                "at_percent": (at_count/length*100) if length else 0,
                "n_percent": (n_count/length*100) if length else 0
            })

except FileNotFoundError:

    data = datetime.now()

    with open("error_log.jsonl", "a") as log:
        json_str = json.dumps(data, default=str)
        log.write(f"{json_str} ERROR FileNotFoundError filename={filename}\n")

    print("File not found.")
    exit()

# -------------------------
# DATASET STATISTICS
# -------------------------

lengths = [seq["length"] for seq in all_sequences]
gc_values = [seq["gc_percent"] for seq in all_sequences]

total_bases = sum(lengths)

print("\nDATASET SUMMARY")
print("----------------------")

print(f"Total sequences: {seq_number}")
print(f"Total bases: {total_bases}")

print(f"Min length: {min(lengths)}")
print(f"Max length: {max(lengths)}")
print(f"Average length: {statistics.mean(lengths):.2f}")

if len(lengths) > 1:
    print(f"Median length: {statistics.median(lengths)}")

print("\nBASE COMPOSITION")
print("----------------------")

print(f"A: {total_A}")
print(f"T: {total_T}")
print(f"G: {total_G}")
print(f"C: {total_C}")
print(f"N: {total_N}")

# -------------------------
# PER-SEQUENCE OUTPUT
# -------------------------

print("\nSEQUENCE STATISTICS")
print("----------------------")

for seq in all_sequences:

    print(f"\nID: {seq['id']}")
    print(f"Length: {seq['length']}")
    print(f"GC%: {seq['gc_percent']:.2f}")
    print(f"AT%: {seq['at_percent']:.2f}")
    print(f"N%: {seq['n_percent']:.2f}")

# -------------------------
# CSV EXPORT
# -------------------------

with open("fasta_results.csv", "w", newline="") as csvfile:

    fieldnames = ["id", "length", "gc_percent", "at_percent", "n_percent"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for seq in all_sequences:
        writer.writerow(seq)

print("\nResults written to fasta_results.csv")

# -------------------------
# VISUALIZATION
# -------------------------

plt.figure()
plt.hist(lengths, bins=20)
plt.title("Sequence Length Distribution")
plt.xlabel("Sequence Length")
plt.ylabel("Count")
plt.show()

plt.figure()
plt.hist(gc_values, bins=20)
plt.title("GC Content Distribution")
plt.xlabel("GC %")
plt.ylabel("Count")
plt.show()