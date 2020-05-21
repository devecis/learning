def name(word):
    # Write a function that returns the string "One for <name>, one for me!" Where <name> is an argument provided to the function Use f-string if you're using python.for me!" Where <name> is an argument provided to the function Use f-string if you're using python.
    # name = input("What is your name?")
    print(f"One for {word}, one for me!")


def main():
    word = input("What is your name? ")
    name(word)


if __name__ == "__main__":
    main()
