#Medium:
#Using one of the two examples above, add a conditional to only print odd numbers from 1 to n (make it a function, take n as an argument)
#Write it once using continue to exclude it
#Try using a while(True) loop, and use break to exit the loop.

#for num in range(1,11):
 #   print(num)
 
def odd(): #start of my function
    lower_limit = int(input('Pick a starting point: ')) #picking the lower number
    upper_limit = int(input('pick a stopping point: ')) #picking the upper number
    
    for num in range(lower_limit, upper_limit): # For loop for lower and upper number
        if(num%2 != 0): #Math for deciding if it is a odd or even number
            print (num) #printing all the numbers within range
odd() #stopping the function