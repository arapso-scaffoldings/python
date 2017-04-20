import datetime


def add_timedelta_to_day():
        some_night_datetime = datetime.datetime(2017, 4, 3, 5, 1, 1).date()
        print(str(some_night_datetime))
        some_night_datetime = some_night_datetime + datetime.timedelta(days=1)
        print("Night date plus 1 day {}".format(str(some_night_datetime)))

string_date = "2017-05-21"
result_date = datetime.datetime.strptime(string_date, "%Y-%m-%d").date()
print result_date
print result_date + datetime.timedelta(days=1)