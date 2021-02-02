#Given an input tell if someone if the water is boiling. 100C or 212F
boil_far = 212

user = int(input('How hot is your water?(fahrenheit) '))
if user >= boil_far:
    print('Your water is boiling!')
else:
    print('Not yet keep going.')
    
