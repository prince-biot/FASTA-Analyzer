from datetime import datetime
import json

filename = input("Enter filename (.fasta): ")

seq_number = 0
current_header = None

# counters for the current sequence
length = 0
gc_count = 0
at_count = 0
n_count = 0

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
                current_header = line[1:].split()[0] # '>'removed then split(); [0] pulls seq id from list

                # reset counters
                length = 0
                gc_count = 0
                at_count = 0
                n_count = 0

            else:
                length += len(line)
                gc_count += line.count("G") + line.count("C")
                at_count += line.count("A") + line.count("T")
                n_count += line.count("N")

        # store last sequence after file ends
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
        log.write(f"{json_str} ERROR-FileNotFoundError FileName:{filename}\n")
    print("File not found. Try again!")

else:
    print("\nTotal sequences:", seq_number)

    for seq in all_sequences:
        print(f"\nID: {seq['id']}")
        print(f"Length: {seq['length']}")
        print(f"GC%: {seq['gc_percent']:.2f}")
        print(f"AT%: {seq['at_percent']:.2f}")
        print(f"N%: {seq['n_percent']:.2f}")