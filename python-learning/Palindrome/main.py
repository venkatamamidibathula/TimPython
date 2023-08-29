def is_palindrome(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string+=char
    print(string)
    return string.casefold() == string[::-1].casefold()

a=input("Enter a setence")
if is_palindrome(a):
    print("The sentence is a palindrome")
else:
    print("Not a palindrome")

