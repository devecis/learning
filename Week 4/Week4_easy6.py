def leapyear(year):
    # Write a function that returns 'True' if a year is a leap year (else False). Leap years are:
    # on every year that is evenly divisible by 4
    #  except every year that is evenly divisible by 100
    #    unless the year is also evenly divisible by 400
    # year = int(input("What year would you like to check? "))
    if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


def main():
    year = int(input("What year would you like to check? "))
    leapyear(year)


if __name__ == "__main__":
    main()
