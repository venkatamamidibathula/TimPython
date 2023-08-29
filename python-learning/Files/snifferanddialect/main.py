import csv
filename = 'country_info.txt'
with open(filename,encoding='utf-8',newline='') as countrydata:
    sampledata=""
    for i in range(3):
        sampledata += countrydata.readline()
    sample_dailect = csv.Sniffer().sniff(sampledata)
    countrydata.seek(0)
    reader = csv.reader(countrydata,dialect=sample_dailect)
    for row in reader:
        print(f"{row}")

