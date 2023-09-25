class Kettle:
    def __init__(self,name,ctype):
        self.on = False
        self.name = name
        self.ctype = ctype
    def turneddon(self):
        self.on = True


kenwood = Kettle("Kenwood","Wired")
kenwood.turneddon()
buckies = Kettle("Buckies","Wireless")
print("{0.name},{0.ctype},{0.on},{1.name},{1.ctype},{1.on}".format(kenwood,buckies))

