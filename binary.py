i = int(input('What number do you want in binary?')) #input from user
num=[] #empty list to add 1 or 0's too
binary=[256, 128, 64, 32, 16, 8, 4, 2, 1] #Binary numbers
for x in binary: #start of the for loop to figure out what the 1's and 0's are x represents the numbers in the binary list and we are checking in the binary list
    if x > i: #if the binary number is greater than the i 
        num.append(0) #it appends the num list with a 0
    else:
        num.append(1) #it append the num list with a 1
        i -= x # after appending with 1 i = i - x
        print(x) #printing out what numbers in binary list are getting hit
print(num) #printing out the list in binary