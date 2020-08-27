class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

# all months from January to Dec.
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]

# leap years before the given date
def countLeapYears(d):
    years = d.y
    #leap years or not
    if (d.m <= 2):
        years -= 1

    # An year is a leap year if it is a
    # multiple of 4, multiple of 400 and
    # not a multiple of 100.
    return int(years / 4 - years / 100 +
               years / 400)


# days between two given dates
def getDifference(dt1, dt2):

    # initialize count using years and day
    n1 = dt1.y * 365 + dt1.d

    # Add days for months in given date
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]

    # Since every leap year is of 366 days,
    # Add a day for every leap year
    n1 += countLeapYears(dt1)

    # SIMILARLY, COUNT TOTAL NUMBER
    # OF DAYS BEFORE 'dt2'
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)

    # return difference between
    # two counts
    return (n2 - n1)


# Birth Date
dt1 = Date(1, 2, 1996)

# Current Date
dt2 = Date(27, 8, 2020)

years = getDifference(dt1, dt2) / 365
print("Number of years is: ")
print(round(years))

months = getDifference(dt1, dt2) / 12
print("Number of months is: ")
print(round(months))

print("Number of days is: " )
print(getDifference(dt1, dt2))


