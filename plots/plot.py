"""File for abstract Plot class
"""

from environment.terraformer import Terraformer
from environment.terraformer_old import TerraformerOld
from helpers.misc import Misc
from environment.coord import Coord
from utils.settings import DEFAULT_TERRAFORM_ALGORITHM

__author__ = "Jacob Eisho"


class Plot:
    """
    Base class for CirclePlot and RectanglePlot
    Provides some useful methods and structures for the plots upon which terraforming will be done,
    and houses will be constructed.
    """

    def __init__(self, start=Coord(0, 0, 0), end=Coord(0, 0, 0)):
        """
        Initialises the plot object
        :param start: Bottom left corner of the plot
        :param end: Top right corner of the plot
        :var points: List of Coord objects that lie within the plot - the plot's 'floor'
        :var pointsToIgnore: List of Coord objects that should be ignored in the plot - i.e. non-floor blocks
        """
        self.start = start
        self.end = end
        self.minHeight = 0
        self.maxHeight = 0
        self.points = []
        self.pointsToIgnore = []
        self.sub_plots = []
        self.refreshPoints()

    def getCentre(self):
        """
        Returns the centre coordinate of the plot
        :return: a Coord object
        """
        return Coord((self.start.x + self.end.x) // 2,
                     Misc.getHeight(((self.start.x + self.end.x) // 2), ((self.start.z + self.end.z) // 2)),
                     (self.start.z + self.end.z) // 2)

    def getCorners(self):
        """
        Returns the 4 corners of the plot
        Bottom left, top left, bottom right, top right
        :return: list of 4 Coord objects
        """
        return [self.start, Coord(self.start.x, self.start.y, self.end.z),
                Coord(self.end.x, self.start.y, self.start.z), self.end]

    def getLengthForHouse(self):
        """
        Length of house
        Default is difference in x-axis
        :return: int
        """
        return self.getLength()

    def getWidthForHouse(self):
        """
        Width of house
        Default is difference in z-axis
        :return: int
        """
        return self.getWidth()

    def getLength(self):
        """
        Length of house
        Default is difference in x-axis
        :return: int
        """
        return abs(self.end.x - self.start.x)

    def getWidth(self):
        """
        Width of house
        Default is difference in z-axis
        :return: int
        """
        return abs(self.end.z - self.start.z)

    def terraform(self):
        """
        Performs terraforming on the plot based on the algorithm in settings.py
        :return: None
        """
        if DEFAULT_TERRAFORM_ALGORITHM == 1:
            TerraformerOld.doTerraformingOld(self)
        elif DEFAULT_TERRAFORM_ALGORITHM == 2:
            TerraformerOld.doTerraforming(self)
        elif DEFAULT_TERRAFORM_ALGORITHM == 3:
            success = Terraformer.doTerraforming(self)
            # Fallback to old terraforming algorithm if bilateral filter was unsuccessful
            if not success:
                TerraformerOld.doTerraforming(self)

    def getCoordsForHouse(self):
        """
        Will be overwritten by children
        """
        pass

    def getAllPoints(self):
        """
        Will be overwritten by children
        """
        pass

    def getPerimeter(self):
        """
        Will be overwritten by children
        """
        pass

    def refreshPoints(self):
        """
        Will be overwritten by children
        """
        pass

    def contains(self, point):
        """
        Check if a given coord lies within the plot
        :param point: Coord object
        :return: True if point lies within plot, False otherwise
        """
        return (self.start.x <= point.x <= self.end.x and
                self.start.z <= point.z <= self.end.z)
