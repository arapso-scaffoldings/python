
a, b = "a", "b"

print a + b

def test():
    while True:
        yield 1
        break

result = test()
for temp in result:
    print temp