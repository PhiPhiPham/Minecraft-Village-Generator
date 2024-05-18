"""File for Trace class
"""

import math
from environment.coord import Coord
from utils.settings import DEFAULT_TERRAIN_SMOOTHING_RESOLUTION
from helpers.misc import Misc

__author__ = "Jacob Eisho"


class Trace:
    """
    Trace static class
    """
    @staticmethod
    def traceCircle(centre=Coord(), r=DEFAULT_TERRAIN_SMOOTHING_RESOLUTION):
        """
        Returns a list of Coord objects for every point that lies on the circumference of a circle
        :param centre: centre Coord of circle
        :param r: radius of circle
        :return: list of Coord objects
        """
        coordinates = []
        x, z = centre.x, centre.z
        for i in range(360):
            angle = math.radians(i)
            x_coord = int(round(x + r * math.cos(angle)))
            z_coord = int(round(z + r * math.sin(angle)))
            if (x_coord, z_coord) not in coordinates:
                coordinates.append(Coord(x_coord, Misc.getHeight(x_coord, z_coord), z_coord))
        return coordinates

    @staticmethod
    def traceSphere(coord=Coord(), radius=0):
        """
        Returns a list of Coord objects for every point that lies on the outside of a sphere
        :param coord: centre Coord of sphere
        :param radius: radius of sphere
        :return: list of Coord objects
        """
        coordinates = []
        for x in range(radius * -1, radius):
            for y in range(radius * -1, radius):
                for z in range(radius * -1, radius):
                    if x ** 2 + y ** 2 + z ** 2 < radius ** 2:
                        coordinates.append(Coord(coord.x + x, coord.y + y, coord.z + z))
        return coordinates

    @staticmethod
    def traceRectangle(start=Coord(), end=Coord()):
        """
        Returns a list of Coord objects for every point that lies on the perimeter of a rectangle
        :param start: Bottom left corner of rectangle
        :param end: Top right corner of rectangle
        :return: list of Coord objects
        """
        x1, y, z1 = start.x, start.y, start.z
        x2, z2 = end.x, end.z
        perimeter = []
        # Add all the points on the top and bottom sides of the rectangle
        for x in range(min(x1, x2), max(x1, x2)+1):
            perimeter.append(Coord(x, y, z1))
            perimeter.append(Coord(x, y, z2))
        # Add all the points on the left and right sides of the rectangle
        for z in range(min(z1, z2)+1, max(z1, z2)):
            perimeter.append(Coord(x1, y, z))
            perimeter.append(Coord(x2, y, z))
        return perimeter
