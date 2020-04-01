# Let the user enter in 2 numbers and giving all the odd numbers between them.

def odd(lower_limit, upper_limit): #defining odd function
    num_list=[]  #empty list to catch iterated numbers
    i = lower_limit #Lower limit that is being called in the main function
    while (True): #start of the while statement with true
        if (i%2 != 0): #checking if there is a remainder (%+ modulus)
            num_list.append(i) #appending the num list
        i += 1 #adding 1
        if (i > upper_limit): #if i is greater than upper_limit
            break #break
    print(num_list)
   
def main(): #creating main function
    lower_limit = int(input('Pick a starting point: ')) #user inputs lower number
    upper_limit = int(input('pick a stopping point: '))#user inputs upper number
    odd(lower_limit, upper_limit) #runs the odd fuction against lower/upper
    
if __name__ == '__main__':
    main()