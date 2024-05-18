"""File for miscellaneous helper classes
"""

from mcpi.minecraft import Minecraft
import time

__author__ = "Jacob Eisho"


class Misc:
    """
    Misc static class, helper for our other classes
    """
    mc = Minecraft.create()

    @staticmethod
    def tpToSpawn():
        """
        Teleport player to world spawn
        :return: none
        """
        Misc.mc.player.setPos(Misc.spawnCoords())
        return

    @staticmethod
    def playerCoords():
        """
        :return: x-, y-, z-coordinates of player
        """
        return Misc.mc.player.getPos()

    @staticmethod
    def spawnCoords():
        """
        Get world spawn coords
        Always x=0. z=0 unless manually changed by player
        :return: tuple of int
        """
        return 0, Misc.mc.getHeight(0, 0), 0

    @staticmethod
    def getHeight(x, z):
        """
        :param x: x-coord
        :param z: z-coord
        :return: y-level of the highest non-air block at x, z
        """
        return Misc.mc.getHeight(x, z)

    @staticmethod
    def getBlock(x, y, z):
        """
        Get the id of the block at x, y, z
        :param x: x-coord
        :param y: y-coord
        :param z: z-coord
        :return: int id of block
        """
        return Misc.mc.getBlock(x, y, z)

    @staticmethod
    def placeWater(x, y, z):
        """
        Place water at x, y, z and remove after 5 seconds
        :param x: x-coord
        :param y: y-coord
        :param z: z-coord
        :return: none
        """
        Misc.mc.setBlock(x, y, z, 9)
        time.sleep(5)
        Misc.mc.setBlock(x, y, z, 0)
        return

    @staticmethod
    def getHeights(x1, z1, x2, z2):
        """
        Get heights of world between (x1, z1) and (x2, z2)
        :param x1: x-coord start corner
        :param z1: z-coord start corner
        :param x2: x-coord end corner
        :param z2: z-coord end corner
        :return: list of y-values
        """
        return Misc.mc.getHeights(x1, z1, x2, z2)

    @staticmethod
    def getBlocks(x1, y1, z1, x2, y2, z2):
        """
        Get blocks of world between (x1, z1) and (x2, z2)
        :param x1: x-coord start corner
        :param y1: y-coord start corner
        :param z1: z-coord start corner
        :param x2: x-coord end corner
        :param y2: y-coord end corner
        :param z2: z-coord end corner
        :return: list of block ids
        """
        return Misc.mc.getBlocks(x1, y1, z1, x2, y2, z2)

    @staticmethod
    def setBlock(x, y, z, i):
        """
        Set block at (x, y, z) to id i
        :param x: x-coord
        :param y: y-coord
        :param z: z-coord
        :param i: block id
        :return: None
        """
        return Misc.mc.setBlock(x, y, z, i)
