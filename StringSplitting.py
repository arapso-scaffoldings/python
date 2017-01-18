a = " a, as , , a "


temp = a.split(",")
print temp
res = filter(None, [ b.strip() for b in temp])


res2 = filter(None, a.replace(" ", "").split(","))

print res
print res2
