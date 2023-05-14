from datetime import datetime
import random

date_format = "%Y-%m-%d"


def random_date():
    d1 = None
    d2 = None

    while True:
        d1 = datetime.strptime(input("Enter 1st Date (YYYY-MM-DD):"), date_format)
        d2 = datetime.strptime(input("Enter 2st Date (YYYY-MM-DD):"), date_format)
        if bool(d1) and bool(d2):
            break
        else:
            print("wrong format")

    return d1 + (d2 - d1) * random.random()


def main():
    if random_date().weekday() == 0:
        print("I don't have vinaigrette")
    return 0


if __name__ == '__main__':
    main()
