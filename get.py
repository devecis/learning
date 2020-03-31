performances = {'Ventriloquism':'9:00am', 
               'Snake Charmer': '12:00pm', 
               'Amazing Acrobatics': '2:00pm', 
               'Bearded Lady':'5:00pm'}
showtime = performances.get('Bearded Lady') # use XXX.get('item) to ensure that the program doesn't return an error
if (showtime == None):
    print ("Performance doesn't exist")
else:
    print('The time of the Bearded Lady show is ', showtime)