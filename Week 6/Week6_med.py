# Write a function that returns True if a number is Prime, and False if a number is nonprime.
# given a Number
# check for factors to number
# if true return true
# if false return false


def primer():
    num = 230
    prime = []
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                prime.append('false')
                break
        else:
            prime.append('true')
    return(prime)


def main():
    print(primer())


if __name__ == "__main__":
    main()
