import os
import timeit


from core.TempFileGenerator import TempFileGenerator
from core.IpGenerator import IpGenerator


class App:
    def start(self):
        temp = TempFileGenerator()
        temp.generate(['file1', 'file2', 'file3', 'file4', 'file5'])

        ipGen = IpGenerator()
        ips = ipGen.generate(4)
        print ips

app = App()
app.start()

setExample = set(range(4))
setExample.add(1)
print setExample

for i in setExample:
    print i