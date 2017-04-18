import luigi
from luigi.contrib.simulate import RunAnywayTarget
from luigi.parameter import Parameter
from luigi.s3 import S3Client
from luigi.util import inherits


class DeleteRecursively(luigi.Task):
    priority = 100

    path = Parameter(description="The path which will be deleted from S3")

    def output(self):
        return RunAnywayTarget(self)

    def run(self):
        s3_client = S3Client()
        s3_client.remove(self.path, recursive=True)
        self.output().done()

@inherits(DeleteRecursively)
class ParentTask(luigi.WrapperTask):

    def run(self):
        print "Hello i am parent"

    def requires(self):
        return self.clone(DeleteRecursively)

