import csv

with open('OlympicMedals_2020.csv',encoding='utf-8',newline='') as csvcontent:
    headers = csvcontent.readline().strip('\n').split(',')
    print(f"{headers}")
    reader = csv.reader(csvcontent,quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)