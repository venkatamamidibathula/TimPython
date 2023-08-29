list1 = ["Red","Blue","Green","Violet","Red","Violet","Pink"]

# To get unique values of lis1

list2 = set(list1)

print(list2)

# Incase i want to get unique values and also preserve the insertion order

list2 = list(dict.fromkeys(list1))

print(list2)
