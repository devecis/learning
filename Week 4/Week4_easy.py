# Make a function that returns if a number is even (And false if it is odd).
# Ask user to input a number
# see it number is even
# if even return True or if odd return false


# def even_odd(num):
#     # num = int(input("Is the number even?"))
#     if (num % 2) == 0:
#         print(num, "is even")
#     else:
#         print(num, " is odd")


# def multi(raw):
#     # Write a function that prints the multiplication tables from 1 to 12. (Use two loops, one within the other!)
#     # Ask the user if they want a multiplication table
#     # If no quit
#     # If yes print out multiplication table 1 to 12

#     # raw = int(input("What numbers multiplication table would you like? "))
#     for i in range(1, 13):
#         print(raw, "x", i, "=", raw * i)


# def name(name):
#     # Write a function that returns the string "One for <name>, one for me!" Where <name> is an argument provided to the function Use f-string if you're using python.for me!" Where <name> is an argument provided to the function Use f-string if you're using python.
#     # name = input("What is your name?")
#     print(f"One for {name}, one for me!")


# def reverse(rev):
#     # write a function that reverses a string (And don't use str.reverse()... Cheaters... )
#     rev = print(input("Give me something ")[::-1])


def leapyear(year):
    # Write a function that returns 'True' if a year is a leap year (else False). Leap years are:
    # on every year that is evenly divisible by 4
    #  except every year that is evenly divisible by 100
    #    unless the year is also evenly divisible by 400
    # year = int(input("What year would you like to check? "))
    if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, " nope")


def main():
    pick = int(input("What do you want to do, even/odd number (1), find a multiplication table (2), prove that I know how to use a f-string (3), write your phrase backwards (4), find out if a year is leap or not (5) "))
    if pick == "1":
        num = int(input("Is the number even?"))
        even_odd(num)
    if pick == "2":
        raw = int(input("What numbers multiplication table would you like? "))
        multi(raw)
    if pick == "3":
        name = input("What is your name?")
        name(name)
    if pick == "4":
        print(input("Give me something ")[::-1])
    if pick == "5":
        year = int(input("What year would you like to check? "))
        leapyear(year)
main()