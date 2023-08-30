import csv
input_file = 'country_info.txt'
countries={}
with open(input_file,encoding='utf-8',newline='',mode='r') as country_data:
    filecontent = csv.DictReader(country_data, delimiter='|')
    for row in filecontent:
        countries[row['Country'].casefold()]=row
        countries[row['CC'].casefold()] = row
print(countries)
while True:
     user_input = input("Enter the country/cc you wish to find the capital city:\n").casefold()
     if user_input in countries:
         print(countries[user_input].get('Capital'))
     else:
         user_input = False
         break
