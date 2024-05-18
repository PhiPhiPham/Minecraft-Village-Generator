"""File for BuildPlot class
"""
from environment.coord import Coord
from plots.plot import Plot
from mcpi.minecraft import Minecraft
from structures.house import buildHouse

__author__ = "Jacob Eisho"


class Builder:
    """
    BuildPlot class
    """
    def __init__(self, plot=Plot()):
        """
        Initialise the MCPI connection
        :param plot: plot upon which building is to take place
        """
        self.plot = plot
        self.is_built = False
        self.door_coords = Coord()
        self.mc = Minecraft.create()

    def buildOutline(self):
        """
        Builds an outline surrounding the plot boundaries
        :return: None
        """
        coords = self.plot.getPerimeter()
        for coord in coords:
            self.mc.setBlock(coord.x, self.mc.getHeight(coord.x, coord.z), coord.z, 1)

    def buildHouse(self):
        """
        Builds a house inside the plot boundaries
        :return: None
        """
        if not self.is_built:
            self.door_coords = buildHouse(self.plot)
            self.is_built = True
        else:
            print("Plot already has a building!")
