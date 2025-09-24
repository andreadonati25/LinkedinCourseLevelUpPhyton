import csv

def unite_CSV(*in_path, output_path="merged.csv"):
    fieldnames = []
    for file in in_path:
        with open(file, 'r') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)

    with open(output_path, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in in_path:
            with open(file, 'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)

unite_CSV("Ex12_class1.csv", "Ex12_class2.csv", output_path="Ex12_final.csv")