class Dog:
    
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
d.kind                  # shared by all dogs

e.kind                  # shared by all dogs

d.name                  # unique to d

e.name                  # unique to e