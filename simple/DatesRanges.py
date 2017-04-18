import datetime

if __name__ == "__main__":
    print "Dates example"

    temp = datetime.date.today()
    print temp

    i = 0
    while i < 10:
        day_before = datetime.timedelta(i)
        print temp - day_before
        i = i + 1
