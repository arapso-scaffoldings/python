import luigi
import tempfile
from luigi.util import inherits

class TempFileTask(luigi.Task):
    tempDir = tempfile.mkdtemp()

    test = luigi.Parameter()

    def run(self):
        print self.tempDir
        with self.output().open("w") as temp:
            temp.write("OKOKOK\n")

    def output(self):
        return luigi.LocalTarget(self.tempDir + "/temp.txt")

@inherits(TempFileTask)
class ParentTask1(luigi.WrapperTask):

    def run(self):
        print "Hello i am parent 1"

    def requires(self):
        return TempFileTask()

@inherits(TempFileTask)
class ParentTask2(luigi.WrapperTask):

    def run(self):
        print "Hello i am parent 2"

    def requires(self):
        return TempFileTask()

@inherits(ParentTask1)
class ChildWithBool(luigi.WrapperTask):

    bool_param = luigi.BoolParameter(default=False)

    def requires(self):
        if self.bool_param:
            return ParentTask1()
        else:
            return ParentTask2()