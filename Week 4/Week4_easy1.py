def even_odd(num):
    # num = int(input("Is the number even?"))
    if (num % 2) == 0:
        print(num, "is even")
    else:
        print(num, " is odd")


def main():
    num = int(input("Is the number even? "))
    even_odd(num)


if __name__ == "__main__":
    main()