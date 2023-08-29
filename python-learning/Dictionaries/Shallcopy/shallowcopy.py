import copy
california_cities = ["Irvine","Los Angeles","San Diego","San Jose"]
texas_cities = ["Houston","Dallas","San Antonio"]
florida_cities = ["Orlando","Tampa"]

state_cities = {"California":california_cities, "Texas": texas_cities,"Florida": florida_cities}

print(state_cities)

#new_state_cities = state_cities.copy()
new_state_cities = copy.deepcopy(state_cities)

print(new_state_cities)

state_cities["Texas"].append("Austin")

print(state_cities)
print(new_state_cities)