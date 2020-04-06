import random

    num = input("Number of times to flip coin: ")
    recordList = []
    heads = 0
    tails = 1
    for amount in range(num):
         flip = random.randint(0, 1)
         if (flip == 0):
              print("Heads")
              recordList.append("Heads")
         else:
              print("Tails")
              recordList.append("Tails")
    print(str(recordList))
    print(str(recordList.count("Heads")) + str(recordList.count("Tails")))