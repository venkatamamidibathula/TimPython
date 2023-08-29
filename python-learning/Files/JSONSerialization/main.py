import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]


# to create a json file

with open('test.json','w') as testfile:
    json.dump(languages,testfile)

# To make use of contents from the JSON file

with open('test.json','r') as testfile:
    data = json.load(testfile)
    print(data[3])