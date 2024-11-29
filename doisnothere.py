import csv

# Read the text from which the DOIs are searched for (plain text file, e.g. conference-archive.md)
with open('text_file_name.md', 'r', encoding='utf-8') as file:
    text = file.read()

# Read the unique strings (DOIs) from the CSV file
# These can be extracted from the API with zenodotocvs.py
unique_strings = []
with open('unique_strings.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        unique_strings.append(row[0])

# List of strings to be excluded
# Community may included double entries or additional related files. If these are not in the text, they can be excluded here.
# e.g. 10.5281/zenodo.xxx is an identified double
# e.g. 10.5281/zenodo.yyy is a supplementary file and not linked from the website
escaped_strings = ["DOI", "10.5281/zenodo.xxx", "10.5281/zenodo.yyy"]

# Find strings that do not appear in the text and are not in the escaped list
missing_strings = [s for s in unique_strings if s not in text and s not in escaped_strings]

print("Strings not found in the text file provided:", missing_strings)