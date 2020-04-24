# Write a function that returns only numbers that are divisible by 3 and 5, below a given limit, like isdivisible(100) returns 15,30,45,60,75,100.

num = int(input("Below what number would you like to see is divisble by 3 and 5? "))
isdiv = []
for i in range(1, num):
    if (i%3 ==0) and (i%5 ==0):
        isdiv.append(i)
print(isdiv)