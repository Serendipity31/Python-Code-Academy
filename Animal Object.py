#Create a class called animals, and create three instances of this class:
#hippos, sloth, and ocelot. Each has two attributes: name and age.

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Alan", 29)
print hippo.description()

sloth = Animal("Belt", 2)
ocelot = Animal("Larry", 4)

print hippo.health
print sloth.health
print ocelot.health