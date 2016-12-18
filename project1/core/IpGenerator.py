import random

class IpGenerator:
    def generate(self, num):
        list = []
        for i in range(num):
            list.append(".".join([(lambda: random.Random().randint(1, 255).__str__())() for _ in range(4)]))
        return list