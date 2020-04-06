#Write a function that flips a coin. It should return a string that reads 'Heads' or 'Tails'. Bonus points if you add the ability to make the coin unfair.
import random

coin = input("How many times would you like to flip the coin or Q to quit: ")
head=0
tail=1
detail=[]
for times in range(coin):
    flip=random.randint(0,1)
    if (flip == 0):
        detail.append('heads')
    else:
        detail.append('Tails')
print(detail)
    

#import random
#def coinToss(number):
#    number = input
#    recordList = [0,1]
#    heads = 0
#    tails = 1
#    flip = random.random()
#    if (flip == 0):
#        print("Heads")
#        recordList.append("Heads")
#    else:
#        print("Tails")
#        recordList.append("Tails")
#    print(str(recordList))
#    print(str(recordList.count("Heads")) + str(recordList.count("Tails")))