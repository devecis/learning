def multi(raw):
    # Write a function that prints the multiplication tables from 1 to 12. (Use two loops, one within the other!)
    # Ask the user if they want a multiplication table
    # If no quit
    # If yes print out multiplication table 1 to 12

    # raw = int(input("What numbers multiplication table would you like? "))
    for i in range(1, 13):
        print(raw, "x", i, "=", raw * i)


def main():
    raw = int(input("What numbers multiplication table would you like? "))
    multi(raw)


if __name__ == "__main__":
    main()
