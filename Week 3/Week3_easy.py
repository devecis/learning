# Write a function that flips a coin. It should return a string that reads 'Heads' or 'Tails'. Bonus points if you add the ability to make the coin unfair.
import random


def coinflip(coin):
    detail = []
    # flip=random.randint(0,1)
    for i in range(coin):
        flip = random.randint(0, 1)
        if flip == 0:
            detail.append("Heads")
        else:
            detail.append("Tails")
    print(detail)
    print(
        str("You got Heads"),
        detail.count("Heads"),
        str("times and you got tails"),
        detail.count("Tails"),
        str("times."),
    )


def main():
    coin = 5  # int(input("How many times would you like to flip the coin: "))
    coinflip(coin)


if __name__ == "__main__":
    main()
