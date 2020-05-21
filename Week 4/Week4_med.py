# Write a class!
# I want a 'vehicle' class, that has a data structure for
# seats (Maybe a list of lists? A dict of lists?), and attributes like
# weight,
#  fuel capacity. Write functions to allow the setting and getting of these attributes. Bonus points if you sort out a way to store passengers in seats.
# See here: https://docs.python.org/3/tutorial/classes.html


from pprint import pprint
class Vehicles:
    """ For defining vehicles"""

    def __init__(self, make, seat_rows, seat_columns, weight, fuel_capacity):
        self.type = make
        self.row = seat_rows
        self.column = seat_columns
        self.weight = weight
        self.fuel_cap = fuel_capacity
                   
        self.grid = {}
        for rows in range(seat_rows):
            seats = []
            for cols in range(seat_columns):
                seats.append(None)
                self.grid.update({rows: seats})

C130 = Vehicles('lockheed', 40, 5, 4324323424, 40000)
pprint(C130.grid)
