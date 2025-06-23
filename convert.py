import csv

with open("top-1m.csv", "r", newline='', encoding='utf-8') as infile, \
     open("phishing_dataset.csv", "w", newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) >= 2:
            new_row = [f"https://{row[1]}/", "0"]
            writer.writerow(new_row)
print("✅ New URL s succesfully added.")