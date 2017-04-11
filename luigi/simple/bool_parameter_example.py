import luigi
import tempfile


class TempFileTask(luigi.Task):
    tempDir = tempfile.mkdtemp()

    def run(self):
        print self.tempDir
        with self.output().open("w") as temp:
            temp.write("OKOKOK\n")

    def output(self):
        return luigi.LocalTarget(self.tempDir + "/temp.txt")


class ParentTask1(luigi.WrapperTask):

    def run(self):
        print "Hello i am parent 1"

    def requires(self):
        return TempFileTask()


class ParentTask2(luigi.WrapperTask):

    def run(self):
        print "Hello i am parent 2"

    def requires(self):
        return TempFileTask()


class ChildWithBool(luigi.WrapperTask):

    bool_param = luigi.BoolParameter(default=False)

    def requires(self):
        if self.bool_param:
            return ParentTask1()
        else:
            return ParentTask2()