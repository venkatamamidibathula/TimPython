countries = {}
with open('country_info.txt', 'r') as countryfile:
    countryfile.readline()
    for row in countryfile:
        country_info = row.strip('\n').split('|')
        country,capital,cc,cc3,code,timezone,currency = country_info
        country_dict = {
            'name': country,
            'capital': capital,
            'CountryCode': cc,
            'Country Code3': cc3,
            'timezone': timezone,
            'currency': currency
        }
        countries[country.casefold()]= country_dict
        countries[cc.casefold()]=country_dict
print(countries)

while True:
    user_input = input("Enter the country/cc you wish to find the capital city:\n").casefold()
    if user_input in countries:
        print(countries[user_input].get('capital'))
    else:
        user_input = False
        break


