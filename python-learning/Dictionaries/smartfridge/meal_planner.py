from contents import pantry,recipes
dict_recipe = {}
for index, key in enumerate(recipes):
    dict_recipe[str(index+1)] = key

while True:
    print("Please choose your recipe")
    print("--------------------------")
    for key,value in dict_recipe.items():
        print(f"{key}- {value}")
    choice = input(":")
    if choice == "0":
        break
    elif choice in dict_recipe:
        selected_item = dict_recipe[choice]
        print(f"You have selected {selected_item}")
        ingredients = recipes[selected_item]
        print(f"The ingredients required are {ingredients}")
        for food_item in ingredients:
            if food_item in pantry:
                print(f"\t {food_item } OK ....")
            else:
                print(f"\t {food_item} not available")





