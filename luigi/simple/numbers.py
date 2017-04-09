# Filename: run_luigi.py
import luigi


class BaseConfig(luigi.Config):
    file_prefix = luigi.Parameter(default="prefix")
config = BaseConfig()


class NumberParameter():
    n = luigi.IntParameter(default=10)


class PrintNumbers(luigi.Task, NumberParameter):
    name = "numbers"

    def output(self):
        return luigi.LocalTarget("numbers_up_to_{}.txt".format(self.n))

    def run(self):
        with self.output().open('w') as f:
            for i in range(1, self.n + 1):
                f.write("{}\n".format(i))


class FibonacciNumbers(luigi.Task, NumberParameter):
    name = "fibonacci"

    def output(self):
        return luigi.LocalTarget("fibonacci_{}.txt".format(self.n))

    def run(self):
        with self.output().open("w") as f:
            left = 0
            right = 1
            for i in range(1, self.n + 1):
                temp = right + left
                f.write("{}\n".format(temp))
                left = right
                right = temp


class SquaredNumbers(luigi.Task, NumberParameter):
    parent_task = luigi.TaskParameter(default=PrintNumbers)

    def requires(self):
        yield self.clone(self.parent_task)

    def output(self):
        return luigi.LocalTarget("squares_{}_{}.txt".format(self.n, self.parent_task.name))

    def run(self):
        for input in self.input():
            with input.open() as fin:
                with self.output().open('w') as fout:
                    for line in fin:
                        n = int(line.strip())
                        out = n * n
                        fout.write("{}:{}\n".format(n, out))

if __name__ == '__main__':
    luigi.run()
