
choice = "-"
while choice != '0':
    if choice in set("123456"):
        print(f"The choice entered is valid choice {choice}")
    else:
        print("Enter a valid choice")
        print("0: To Exit")
        print("1: To learn Python")
        print("2: To learn Java")
    choice = input()

