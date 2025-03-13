#load_csv function
import csv


def load_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile) #dictionary reader
        data = list(reader)  
    return data
#opens the csv file and puts the data into a list of dictionaries

