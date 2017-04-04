from collections import defaultdict

if __name__ == "__main__":
    temp = defaultdict(set)

    temp["asd"].add("a")
    temp["asd"].add("b")
    temp["asd"].add("c")
    temp["asd"].add("d")
    temp["asd"].add("e")

    print temp