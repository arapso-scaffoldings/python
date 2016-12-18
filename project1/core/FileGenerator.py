class FileGenerator:

    def __init__(self, path = "/tmp/"):
        self.path = path

    def generate(self, n):
        for i in n:
            with open("{}{}".format(self.path, i),  mode='w') as file:
                file.write("%s"%i)
