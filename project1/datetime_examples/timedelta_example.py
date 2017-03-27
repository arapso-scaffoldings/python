import datetime

endDate = datetime.date(2017,02,28)
startDate = endDate - datetime.timedelta(days=32)
delta = datetime.timedelta(days=1)
temp = startDate
i = 0
while temp != endDate:
    i += 1
    print "%s-%s" % (i, temp)
    temp = temp + delta