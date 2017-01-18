

class Params(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s %s"% (self.name, self.age)

    def __repr__(self):
        return "%s %s"% (self.name, self.age)

class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s %s"% (self.name, self.age)

    def __repr__(self):
        return "%s %s"% (self.name, self.age)



AvailableFamilyModes = {
    "singiel": [
        Params("Damian", 21)
    ],
    "rodzinka": [
        Params("Arek", 11),
        Params("Pawel", 28),
        Params("Ela", 32)
    ],
    "malzenstwo": [
        Params("Dominika", 18),
        Params("Henryk", 34)
    ]
}



def makeFamilyByType(type):
    params = AvailableFamilyModes.get(type)
    print params
    array = [Human(n.name, n.age) for n in params]
    print array

makeFamilyByType("singiel")


makeFamilyByType("malzenstwo")