# Write a function that returns all of the elements of a list that are odd.
# Given a list of number,
# if each number is not evenly divided by 2 return the odd numbers to a list
# return list.


def odd_num():
    num = 100
    odds = []
    for i in range(1, num):
        if i % 2 != 0:
            odds.append(i)
    return(odds)

def main():
    print(odd_num())

if __name__ == "__main__":
    main()
