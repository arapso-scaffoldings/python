
class Type(object):
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

    def __repr__(self):
        return "%s %s" % (self.name, self.temp)

list = [Type("a", "adsd"), Type("b", "ewadsdasd"), Type("a2", "adsd")]


g = ['a', 'b']


filtered = filter(lambda x: g.__contains__(x.name), list)

print filtered