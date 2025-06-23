import csv

# Giriş dosyası: Eklemek istediğin veriler
input_file = "PhiUSIIL_Phishing_URL_Dataset.csv"

# Var olan CSV dosyası: URL ve etiket içeren dosya
existing_file = "phishing_dataset.csv"

# Okuma + yazma işlemi
with open(input_file, "r") as infile, open(existing_file, "a", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) >= 2:
            url = row[1].strip()
            writer.writerow([url, 1])  # Etiket daima 1 olacak

print("✅ New URL s succesfully added.")
