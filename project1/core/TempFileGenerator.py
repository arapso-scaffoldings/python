import uuid
import os
import os.path as path

class TempFileGenerator:

    def __init__(self, dir_path ="/tmp/"):
        assert not path.exists(dir_path), "Temporary folder should not exists"
        self.dir_path = dir_path

    def generate(self, n):
        os.makedirs(self.dir_path)
        for i in xrange(n):
            self.__create_file(self.dir_path, i, i)

    def __create_file(self, dir_path, file_name, content):
        with open(path.join(dir_path, str(file_name)), mode='w') as file:
            file.write("%s" % str(content))

if __name__ == "__main__":
    print "Temporary file generator script"

    ''':type tempFolder: path'''
    tempFolder = path.join("/tmp/python", str(uuid.uuid4()))

    ''':type generator: TempFileGenerator'''
    generator = TempFileGenerator(tempFolder)
    generator.generate(10)

    assert path.exists(tempFolder), "Folder should be created by temp file generator"
    list = os.listdir(tempFolder)
    print list