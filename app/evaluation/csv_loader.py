import csv

def load_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)  
    return data

