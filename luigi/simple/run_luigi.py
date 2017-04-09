# Filename: run_luigi.py
import luigi


class BaseConfig(luigi.Config):
    file_prefix = luigi.Parameter(default="prefix")
config = BaseConfig()


class PrintNumbers(luigi.Task):
    name = "numbers"
    n = luigi.IntParameter(default=10)

    def output(self):
        return luigi.LocalTarget("numbers_up_to_{}.txt".format(self.n))

    def run(self):
        with self.output().open('w') as f:
            for i in range(1, self.n + 1):
                f.write("{}\n".format(i))


class FibonnaciNumbers(luigi.Task):
    name = "fibonnaci"
    n = luigi.IntParameter(default=10)
    def output(self):
        return luigi.LocalTarget("fibonnaci_{}.txt".format(self.n))

    def run(self):
        with self.output().open("w") as f:
            left = 0
            right = 1
            for i in range(1, self.n + 1):
                temp = right + left
                f.write("{}\n".format(temp))
                left = right
                right = temp


class SquaredNumbers(luigi.Task):
    n = luigi.IntParameter(default=10)
    parent_task = luigi.TaskParameter(default=PrintNumbers)

    def requires(self):
        return [self.clone(self.parent_task)]

    def output(self):
        return luigi.LocalTarget("squares_{}_{}.txt".format(self.n, self.parent_task.name))

    def run(self):
        with self.input()[0].open() as fin, self.output().open('w') as fout:
            for line in fin:
                n = int(line.strip())
                out = n * n
                fout.write("{}:{}\n".format(n, out))

if __name__ == '__main__':
    luigi.run()
