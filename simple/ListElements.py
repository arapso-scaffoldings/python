

def use_contain():
    a = ("a", "b", "c", "d")
    b = ("b", "c", "a")
    print set(a) == set(b)

    req = ["b", "a"]

    avail = ["a" , "b"]
    print reduce(lambda x, y:x and y, [avail.__contains__(a) for a in req])


def use_of_in():
    avail = ("a", "b", "c", "d")
    req = ("b", "c", "e")

    print reduce(lambda x, y:x and y, [a in avail for a in req])

use_of_in()