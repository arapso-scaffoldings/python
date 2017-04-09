import luigi

class CurrencyRatesDaily(luigi.Task):
    date = luigi.DateParameter()

    def run(self):
        with self.output().open("w") as file:
            file.write("a")

    def output(self):
        return luigi.LocalTarget("rates-{}.txt".format(self.date))


class CurrencyRatesForInterval(luigi.WrapperTask):

    dates = luigi.DateIntervalParameter()

    def requires(self):
        for date in self.dates:
            yield CurrencyRatesDaily(date=date)
