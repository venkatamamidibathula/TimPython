import csv
with open('my_cereals.csv', encoding='utf-8', newline='') as filedata:
    reader = csv.DictReader(filedata)
    for row in reader:
        print(f"{row}")
