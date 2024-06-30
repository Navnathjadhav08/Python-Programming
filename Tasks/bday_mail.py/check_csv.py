import csv

def check_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        print("CSV Headers:", reader.fieldnames)
        for row in reader:
            print(row)

check_csv('dob.csv')
