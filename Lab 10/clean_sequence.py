import re

# File paths
input_file = "preproinsulin-seq-raw.txt"
output_file = "preproinsulin-seq-cleaned.txt"

with open(input_file, "r", encoding="utf-8") as f:
    content = f.readlines()

cleaned_lines = []

for line in content:
    # Remove lines containing only ORIGIN or //
    if "ORIGIN" in line or "//" in line:
        continue
    
    # Remove line numbers (e.g., 1, 61)
    line = re.sub(r'^\s*\d+\s*', '', line)
    
    # Remove spaces and newlines
    line = line.replace(" ", "").strip()
    
    if line:  # skip if now empty
        cleaned_lines.append(line)

# Join into a single line string
final_output = ''.join(cleaned_lines)

# Save result to file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_output)

print("Cleaning complete! Output saved to", output_file)

# Read the cleaned output
with open(output_file, "r", encoding="utf-8") as f:
    cleaned_data = f.read()

# Get the first 24 characters
first_24_chars = cleaned_data[:24]

# Get characters 25 to 54 (index 24 to 53)
segment_25_54 = cleaned_data[24:54]

# Get characters 25 to 54 (index 55 to 89)
segment_55_89 = cleaned_data[54:89]

# Get characters 25 to 54 (index 24 to 53)
segment_90_110 = cleaned_data[89:110]



# Write first 24 to a file
with open("lsinsulin.txt", "w", encoding="utf-8") as f:
    f.write(first_24_chars)

# Write 25-54 to a file
with open("binsulin.txt", "w", encoding="utf-8") as f:
    f.write(segment_25_54)

# Write 55-89 to a file
with open("cinsulin.txt", "w", encoding="utf-8") as f:
    f.write(segment_55_89)

# Write 90-110 to a file
with open("ainsulin.txt", "w", encoding="utf-8") as f:
    f.write(segment_90_110)

print("First 24 characters saved to first_24.txt")
print("Characters 25 to 54 saved to binsulin-seq-clean.txt")
print("Characters 55 to 89 saved to cinsulin-seq-clean.txt")
print("Characters 90 to 110 saved to ainsulin-seq-clean.txt")