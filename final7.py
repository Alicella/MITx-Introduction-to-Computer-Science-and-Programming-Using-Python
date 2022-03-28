### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
from os import remove


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc

    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """

    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        # Your code here
        self.center_loc = center_loc
        self.tent_loc = [tent_loc]

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        # Your code here
        for tent in self.tent_loc:
            if tent.dist_from(new_tent_loc) < 0.5:
                return False
        self.tent_loc.append(new_tent_loc)
        return True

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        # Your code here

        if tent_loc in self.tent_loc:
            self.tent_loc.remove(tent_loc)
        else:
            raise ValueError

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        # Your code here
        tent_dict = {}
        tents = []
        for tent in self.tent_loc:
            tent_dict[str(tent)] = tent.getX()
        sorted_dict = sorted(tent_dict.items())
        # print(sorted_dict)
        for k, v in sorted_dict:
            tents.append(k)
        return tents


c = MITCampus(Location(1, 2), Location(0, 1))
print(c.add_tent(Location(-1, 2)))
print(c.add_tent(Location(1, -10)))
print(c.add_tent(Location(1, 10)))
print(c.add_tent(Location(1, 20)))
print(c.add_tent(Location(1, 40)))
print(sorted(c.get_tents()))
