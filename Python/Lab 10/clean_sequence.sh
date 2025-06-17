#!/bin/bash

# Input file
input_file="preproinsulin-seq-raw.txt"
# Output file
output_file="preproinsulin-seq-clean.txt"

# Clean the file
#grep -vE "^(ORIGIN|//|[0-9]+)" "$input_file" | tr -d ' \r\n' > "$output_file"
sed 's/ORIGIN//g; s/\/\///g; s/\b1\b//g; s/\b61\b//g' "$input_file" | tr -d ' \r\n' > "$output_file"

# Output confirmation
echo "Cleaned sequence saved to $output_file"
