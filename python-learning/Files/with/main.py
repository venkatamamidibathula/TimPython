with open('Jabberwocky.txt','r') as poem:
    chars = "' Twaesbv"
    line = poem.readline()
    print(line)
    a=line.strip(chars)
    print(a)
