"""File for RectanglePlot class
"""

from plots.plot import Plot
from helpers.trace import Trace
from environment.coord import Coord
from helpers.misc import Misc
from utils.settings import GROUND_BLOCKS

__author__ = "Jacob Eisho"


class VillagePlot(Plot):
    """
    Defines a rectangle plot.
    The house will be built within this rectangle.
    """
    """@Override"""
    def getPerimeter(self):
        """
        Gets the coordinates of the blocks that lie on the perimeter of the plot
        :return: list of Coord objects
        """
        return Trace.traceRectangle(self.start, self.end)

    """@Override"""
    def getCoordsForHouse(self):
        """
        Returns the bottom left and top right corners of the plot where the house will be constructed
        :return: tuple of Coord objects
        """
        res = self.getCorners()
        return res[0], res[2]

    """@Override"""
    def refreshPoints(self):
        """
        Gives all the points in the circle
        :return True if successful, False otherwise
        """
        self.points = []
        heights = Misc.getHeights(self.start.x, self.start.z, self.end.x, self.end.z)
        self.minHeight = min(heights)
        self.maxHeight = max(heights)
        blocks = list(
            Misc.getBlocks(self.start.x, self.minHeight, self.start.z, self.end.x, self.maxHeight, self.end.z))

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
                            self.points.append(point)
                    i += 1

        # Update minHeight and maxHeight
        self.start.y = self.minHeight
        self.end.y = self.maxHeight

    def addSubPlot(self, subp):
        self.sub_plots.append(subp)
        self.pointsToIgnore = self.pointsToIgnore + subp.getHouseCoords()
