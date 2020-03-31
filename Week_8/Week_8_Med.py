#Medium:
#Using one of the two examples above, add a conditional to only print odd numbers from 1 to n (make it a function, take n as an argument)
#Write it once using continue to exclude it
#Try using a while(True) loop, and use break to exit the loop.

#for num in range(1,11):
 #   print(num)
 
def odd():
    lower_limit = int(input('Pick a starting point: '))
    upper_limit = int(input('pick a stopping point: '))
    
    for num in range(lower_limit, upper_limit):
        if(num%2 != 0):
            print (num)
odd()