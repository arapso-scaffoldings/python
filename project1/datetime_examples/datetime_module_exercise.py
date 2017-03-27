import datetime

endDate = datetime.date(2017,02,28)
startDate = endDate - datetime.timedelta(days=32)
delta = datetime.timedelta(days=1)
print startDate
print endDate
print startDate == endDate

temp = startDate
while temp != endDate:
    print temp
    temp = temp + delta

print startDate
print endDate