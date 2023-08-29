# import random
# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
# }

# pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# dict_pantry = dict.fromkeys(pantry_items,0)

# print(dict_pantry)


cities = ["Visakhapatnam","Vijayawada","Guntur","Nellore","Kurnool","Kadapa","Rajahmundry","Kakinada","Tirupati","Eluru","Nidadavole"]
districts = ["Visakhapatnam","Krishna","Guntur","Nellore","Kurnool","Kadapa","East Godavari","East Godavari","Chittor","East Godavari","West Godavari"]

Distict_wise_cities = dict(zip(cities,districts))
print(Distict_wise_cities)

cities_corrected = ["Visakhapatnam","Vijayawada","Guntur","Nellore","Kurnool","Kadapa","Rajahmundry","Kakinada","Tirupati","Eluru","Nidadavole","Bhimavaram"]
districts_corrected = ["Visakhapatnam","Krishna","Guntur","Nellore","Kurnool","Kadapa","East Godavari","East Godavari","Chittor","West Godavari","West Godavari","West Godavari"]

Distict_wise_cities_2 = dict(zip(cities_corrected,districts_corrected))

print(Distict_wise_cities_2)

Distict_wise_cities.update(Distict_wise_cities_2)
print(Distict_wise_cities)