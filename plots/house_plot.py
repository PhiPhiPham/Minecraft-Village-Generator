"""File for CirclePlot class
"""

import math
from helpers.misc import Misc
from plots.plot import Plot
from helpers.trace import Trace
from environment.coord import Coord
from utils.settings import GROUND_BLOCKS

__author__ = "Jacob Eisho"


class HousePlot(Plot):
    """
    Defines a circle plot.
    The house will be built within the largest rectangle that can exist within the circle.
    The main difference between RectanglePlot and CirclePlot is that the terraforming algorithm will be performed
    on the circle.
    """
    """@Override"""
    def __init__(self, start=Coord(), end=Coord()):
        """
        :param start:
        :param end:
        """
        super().__init__(start, end)

    """@Override"""
    def refreshPoints(self):
        """
        Gives all the points in the circle
        :return True if successful, False otherwise
        """
        centre = self.getCentre()

        heights = Misc.getHeights(self.start.x, self.start.z, self.end.x, self.end.z)
        self.minHeight = min(heights)
        self.maxHeight = max(heights)
        blocks = list(Misc.getBlocks(self.start.x, self.minHeight, self.start.z, self.end.x, self.maxHeight, self.end.z))

        circle_points = []
        r = self.getRadius()
        for x in range(int(centre.x - r), int(centre.x + r) + 1):
            for z in range(int(centre.z - r), int(centre.z + r) + 1):
                if (x - centre.x) ** 2 + (z - centre.z) ** 2 <= r ** 2:
                    circle_points.append((int(x), int(z)))

        heights = Misc.getHeights(self.start.x, self.start.z, self.end.x, self.end.z)
        self.minHeight = min(heights)
        self.maxHeight = max(heights)
        blocks = list(Misc.getBlocks(self.start.x, self.minHeight, self.start.z, self.end.x, self.maxHeight, self.end.z))

        # Calculate the x, y, and z ranges of the plot
        x_range = range(min(self.start.x, self.end.x), max(self.start.x, self.end.x) + 1)
        y_range = range(self.minHeight, self.maxHeight + 1)
        z_range = range(min(self.start.z, self.end.z), max(self.start.z, self.end.z) + 1)
        # Loop over all x, y, and z values within the plot
        i = 0
        for y in y_range:
            for x in x_range:
                for z in z_range:
                    if blocks[i] != 0:
                        point = Coord(x, y, z)
                        if blocks[i] in GROUND_BLOCKS:
                            if (x, z) in circle_points:
                                self.points.append(point)
                    i += 1

        # i = 0
        # for x in x_range:
        #     for z in z_range:
        #         point = Coord(x, heights[i], z)
        #         if point not in self.pointsToIgnore:
        #                 self.points.append(point)
        #         i += 1
        self.start.y = self.minHeight
        self.end.y = self.maxHeight

    """@Override"""
    def getPerimeter(self):
        """
        Gives all the points on the perimeter of the largest square that can fit in the circle
        :return
        """
        circle_centre = self.getCentre()
        rect_width = math.sqrt(2 * self.getRadius() ** 2)
        rect_height = rect_width
        x, z = circle_centre.x + int(rect_width / 2), circle_centre.z + int(rect_height / 2)
        rect_top_right = Coord(x, Misc.getHeight(x, z), z)
        x, z = circle_centre.x - int(rect_width / 2), circle_centre.z - int(rect_height / 2)
        rect_bottom_left = Coord(x, Misc.getHeight(x, z), z)
        return Trace.traceRectangle(rect_bottom_left, rect_top_right)

    """@Override"""
    def getLengthForHouse(self):
        """
        Gives the length of the largest square that can fit in the circle
        Bezel to give allowance for terraforming
        :return: int
        """
        return int(math.sqrt(2 * self.getRadius() ** 2))-4

    """@Override"""
    def getWidthForHouse(self):
        """
        Gives the width of the largest square that can fit in the circle
        Width == length
        :return: int
        """
        return self.getLengthForHouse()

    """@Override"""
    def getCoordsForHouse(self):
        """
        Gives the start and end coordinates of the house to be built within the circle's maximal square
        :return: tuple of bottom left and top right Coord objects
        """
        circle_centre = self.getCentre()
        rect_width = self.getWidthForHouse()
        rect_height = self.getLengthForHouse()
        x, z = circle_centre.x - int(rect_width / 2), circle_centre.z - int(rect_height / 2)
        rect_bottom_left = Coord(x, Misc.getHeight(x, z), z)
        x, z = circle_centre.x + int(rect_width / 2), circle_centre.z + int(rect_height / 2)
        rect_top_right = Coord(x, Misc.getHeight(x, z), z)
        return rect_bottom_left, rect_top_right

    def getRadius(self):
        """
        Gives the radius of the circle
        :return: int
        """
        return max(abs((self.start.x - self.end.x) // 2), (abs(self.start.z - self.end.z)) // 2)

    def getCircumference(self):
        """
        Gives all the points on the circumference of the circle
        :return: a list of Coord objects
        """
        return Trace.traceCircle(self.getCentre(), self.getRadius())

    def getHouseCoords(self):
        """
        Returns the coordinates at which a house will exist
        :return: List of Coord objects
        """
        start, end = self.getCoordsForHouse()
        return Trace.traceRectangle(start, end)
