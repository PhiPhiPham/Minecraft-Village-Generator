"""File for Coord class
"""

__author__ = "Jacob Eisho"


class Coord:
    """
    Coord class
    """
    def __init__(self, x=0, y=0, z=0):
        """
        :param x: x-coord
        :param y: y-coord
        :param z: z-coord
        """
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.isGround = 0  # set this to True for cells that should be included in the final path

    def get_neighbours(self):
        """
        Returns a list of adjacent Coord objects to the current Coord object.
        :return: list of adjacent Coord objects
        """
        neighbours = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if dx == dy == dz == 0:
                        continue
                    neighbour = Coord(self.x + dx, self.y + dy, self.z + dz)
                    neighbours.append(neighbour)
        return neighbours

    def distance(self, target):
        """
        Computes the Euclidean distance between two Coord objects.
        :param target: other Coord object
        :return: Euclidean distance between self and other
        """
        dx = self.x - target.x
        dy = self.y - target.y
        dz = self.z - target.z
        return (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5

    def __str__(self):
        """
        :return: x, y, z
        """
        return "x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)

    def __eq__(self, other):
        """
        Compare both coords and return true if they are equal
        :param other: Coord
        :return: True or False
        """
        return int(self.x) == int(other.x) and int(self.y) == int(other.y) and int(self.z) == int(other.z)

    def __lt__(self, other):
        """
        Compare both coords distance to origin and return True if self less than other
        :param other: Coord
        :return: True or False
        """
        origin = Coord(0, 0, 0)
        return self.distance(origin) < other.distance(origin)

    def __contains__(self, other):
        """
        Return True if self in list of coord
        :param other: List of Coord
        :return: True or False
        """
        if self in other:
            return True
        else:
            return False

    def __hash__(self):
        """
        :return: hash value for object
        """
        return hash((self.x, self.y, self.z))
    