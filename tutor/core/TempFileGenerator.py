import uuid
import os
import os.path as path
import threading
from EventGenerator import event_content_gen
import argparse

def number_generator(n):
    for i in xrange(n):
        yield str(i)

def uuid_generator(n):
    for i in xrange(n):
        yield str(uuid.uuid4())

def simple_content_gen():
    return "OK"

def gen_json():
    return "{}"

def json_content_gen(lines_no=10):
    for x in xrange(lines_no):
        yield gen_json()

class TempFileGenerator:

    def __init__(self,
                 dir_path ="/tmp/",
                 file_name_gen=number_generator,
                 content_gen=simple_content_gen,
                 concurrent=True):
        assert not path.exists(dir_path), "Temporary folder should not exists"
        self.dir_path = dir_path
        self.file_name_gen = file_name_gen
        self.content_gen = content_gen
        self.concurrent = concurrent

    def generate(self, n, lines_no=10):
        os.makedirs(self.dir_path)
        for i in self.file_name_gen(n):
            if self.concurrent:
                self.__create_file_concurrent(self.dir_path, i, self.content_gen, lines_no)
            else:
                self.__create_file(self.dir_path, i, self.content_gen, lines_no)

    @staticmethod
    def __create_file_concurrent(dir_path, file_name, content_gen, lines_no=10):
        t = threading.Thread(target=TempFileGenerator.__create_file,
                             args=(dir_path, file_name, content_gen, lines_no))
        t.start()

    @staticmethod
    def __create_file(dir_path, file_name, content_gen, lines_no=10):
        with open(path.join(dir_path, str(file_name)), mode='w') as file:
            for line in content_gen(lines_no):
                file.write("%s\n" % line)

if __name__ == "__main__":
    print "Temporary file generator script"

    ''':type tempFolder: path'''
    tempFolder = path.join("/tmp/python", str(uuid.uuid4()))

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--files-no', type=int, default="20")
    parser.add_argument('--lines-no', type=int, default="10000")
    parser.add_argument('--concurrent', type=bool, default="True")

    args = parser.parse_args()
    files_no = args.files_no
    lines_no = args.lines_no
    concurrent = args.concurrent

    ''':type generator: TempFileGenerator'''
    generator = TempFileGenerator(dir_path=tempFolder,
                                  file_name_gen=uuid_generator,
                                  content_gen=event_content_gen,
                                  concurrent=concurrent)
    generator.generate(files_no, lines_no)

    assert path.exists(tempFolder), "Folder should be created by temp file generator!"
    list = os.listdir(tempFolder)
    assert len(list) == files_no, "Generator did not create expected files number!"
