

substractsGroups = {
    "a": ["sa1", "sa2", "sa3"],
    "b": ["sb1"],
    "c": ["sc1", "sc2"]
}

def getSubstracts(avail):
    types = ["a"]
    if avail:
        types = [a.strip() for a in avail.split(",")]
    arrays = [substractsGroups.get(t, []) for t in types]
    result = reduce(lambda x, y: x + y, arrays)
    if not result:
        return substractsGroups.get("a")
    return result

print getSubstracts("a,b")
print getSubstracts(" a , c ")
print getSubstracts("a")
print getSubstracts(None)
print getSubstracts("")
print getSubstracts("d,e")
print getSubstracts("b,f,g,h")