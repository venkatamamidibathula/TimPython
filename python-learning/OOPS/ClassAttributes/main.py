class Kettle:
    powered_on = 'Electricity'
    def __init__(self,name,ctype):
        self.on = False
        self.name = name
        self.ctype = ctype
    def turneddon(self):
        self.on = True


kenwood = Kettle("Kenwood","Wired")
kenwood.turneddon()
buckies = Kettle("Buckies","Wireless")
# Override the class attribute using instance variable
kenwood.powered_on = 'gas'

# Override the class attribute using class variable
Kettle.powered_on = 'atomic'
print("{0.name},{0.ctype},{0.on},{0.powered_on},{1.name},{1.ctype},{1.on},{1.powered_on}".format(kenwood,buckies))

