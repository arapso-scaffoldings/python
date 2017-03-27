import datetime
import time

string_date = "2017-02-01"

time_struct = time.strptime(string_date, "%Y-%m-%d")
print type(time_struct)

start_date_time = datetime.datetime.strptime(string_date, "%Y-%m-%d")
print start_date_time.date()
print start_date_time