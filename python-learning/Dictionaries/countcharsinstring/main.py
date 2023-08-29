string_to_count = "USA has one of the biggest economies in the world"
word_count = {}
for char in string_to_count.replace(" ","").casefold():
    word_count[char]=word_count.setdefault(char,0)+1

for key,value in word_count.items():
        print(f" The letter {key} occured {value} times")
