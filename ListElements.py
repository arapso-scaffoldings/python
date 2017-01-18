
a = ("a", "b", "c", "d")
b = ("b", "c", "a")
print set(a) == set(b)


req = ["b", "a"]

avail = ["a" , "b"]

print reduce(lambda x, y:x and y, [avail.__contains__(a) for a in req])