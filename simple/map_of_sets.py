from collections import defaultdict

events = defaultdict(set, {
    "1": set(["1", "2", "3", "4", "5"]),
    "2": set(["21", "22", "23"]),
    "3": set(["31", "32", "33"])
})

irrelevant = defaultdict(set, {
    "1": set(["1", "4"]),
    "2": set(["22"])
})


def remove(a, b):
    result = dict()
    for key in a.keys():
        result[key] = a[key].difference(b[key])
    return result

print remove(events, irrelevant)