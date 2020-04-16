# Make a function that returns if a number is even (And false if it is odd).
# Ask user to input a number
# see it number is even
# if even return True or if odd return false

def even_odd():
    num = int(input("Is the number even?"))
    if (num % 2) == 0:
        print(num, "is even")
    else:
        print(num, " is odd")

even_odd()


def multi():
# Write a function that prints the multiplication tables from 1 to 12. (Use two loops, one within the other!)
# Ask the user if they want a multiplication table
# If no quit
# If yes print out multiplication table 1 to 12

    raw = int(input('What numbers multiplication table would you like? '))
    for i in range(1,13):
        print (raw, 'x', i, '=', raw*i)
        
multi()

