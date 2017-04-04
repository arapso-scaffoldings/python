
def StringSplit():
    a = " a, as , , a "


    temp = a.split(",")
    print temp
    res = filter(None, [ b.strip() for b in temp])


    res2 = filter(None, a.replace(" ", "").split(","))

    print res
    print res2

def StringMathers():

    if "." in "damian.adasd":
        print "JEST"

    if "." not in "damian.asds":
        print "nie ma"

StringMathers()