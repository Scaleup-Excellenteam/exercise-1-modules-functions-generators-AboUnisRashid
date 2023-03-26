from datetime import datetime
import random

date_format = "%Y-%m-%d"


def random_date():
    d1 = None
    d2 = None

    while True:
        date1 = '2022-01-01'  # input("Enter 1st Date (YYYY-MM-DD):")
        date2 = '2023-01-01'  # input("Enter 2nd Date (YYYY-MM-DD):")
        d1 = datetime.strptime(date1, date_format)
        d2 = datetime.strptime(date2, date_format)
        if bool(d1) and bool(d2):
            break
        else:
            print("wrong format")

    return d1 + (d2 - d1) * random.random()


if random_date().weekday() == 0:
    print("I don't have vinaigrette")
