class Slave():
    Default_Value = "asd"

    def __init__(self, number):
        self.value = Slave.Default_Value
        self.number = number

    def __str__(self):
        return "(%s,%s)" % (self.value, self.number)

    def __repr__(self):
        return "(%s,%s)" % (self.value, self.number)

array = [Slave(1), Slave(2)]
print str(array)
print array[0]

map = dict((a.number, a) for a in array)
print map

map2 =  { "a": "A", "c":"C", "d":"Dsa" }
print map2