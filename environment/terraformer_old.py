"""File for TerraformerOld class, and old terraforming logic
"""

from mcpi.minecraft import Minecraft
from utils.settings import DEFAULT_TERRAIN_SMOOTHING_RESOLUTION
from helpers.trace import Trace
import mcpi.block as Block

__author__ = "Jacob Eisho"


class TerraformerOld:
    """
    TerraformerOld static class
    """
    mc = Minecraft.create()

    @staticmethod
    def doTerraformingOld(plot):
        """
        Performs terraforming using multiple iterations of Circumferential Mode Filtering
        :param plot: Plot to be terraformed
        :return: None
        """
        # Get corners
        plotPerimeter = plot.getCorners()
        # Append centre
        plotPerimeter.append(plot.getCentre())
        for a in range(0, len(plotPerimeter)):
            coords = Trace.traceCircle(plotPerimeter[a], DEFAULT_TERRAIN_SMOOTHING_RESOLUTION)
            # Get most frequent y level of circle's circumference
            yArr = []
            minHeight = 10000
            for j in range(len(coords)):
                cX, cZ = coords[j].x, coords[j].z
                y = TerraformerOld.mc.getHeight(cX, cZ)
                # Store min y-level for foundation building
                minHeight = y if y < minHeight else minHeight
                # Ignore trees, leaves, etc
                currBlock = TerraformerOld.mc.getBlockWithData(cX, y, cZ)
                if currBlock == Block.GRASS or Block.DIRT or Block.SAND:
                    yArr.append(y)
            yArr.sort(reverse=False)
            modeY = max(set(yArr), key=yArr.count)
            for i in range(len(coords) // 2):
                x, z = coords[i].x, coords[i].z
                x2, z2 = coords[len(coords) - i - 1].x, coords[len(coords) - i - 1].z
                TerraformerOld.mc.setBlocks(x, 255, z, x2, modeY, z2, Block.AIR)
                currY = TerraformerOld.mc.getHeight(x, z)
                TerraformerOld.mc.setBlocks(x, minHeight, z, x2, modeY-1, z2, Block.DIRT)
                TerraformerOld.mc.setBlocks(x, modeY, z, x2, modeY, z2, Block.GRASS)

    @staticmethod
    def doTerraforming(plot):
        """
        Performs terraforming using a single iteration of Circumferential Mode Filtering
        :param plot: Plot to be terraformed
        :return: None
        """
        # Get plot centre
        plotCentre = plot.getCentre()
        coords = Trace.traceCircle(plotCentre, DEFAULT_TERRAIN_SMOOTHING_RESOLUTION)
        # Get most frequent y level of circle's circumference
        yArr = []
        minHeight = 10000
        for j in range(len(coords)):
            cX, cZ = coords[j].x, coords[j].z
            y = TerraformerOld.mc.getHeight(cX, cZ)
            # Store min y-level for foundation building
            minHeight = y if y < minHeight else minHeight
            # Ignore trees, leaves, etc
            currBlock = TerraformerOld.mc.getBlockWithData(cX, y, cZ)
            if currBlock == Block.GRASS or Block.DIRT or Block.SAND:
                yArr.append(y)
        yArr.sort(reverse=False)
        modeY = max(set(yArr), key=yArr.count)
        for i in range(len(coords) // 2):
            x, z = coords[i].x, coords[i].z
            x2, z2 = coords[len(coords) - i - 1].x, coords[len(coords) - i - 1].z
            TerraformerOld.mc.setBlocks(x, 255, z, x2, modeY, z2, Block.AIR)
            currY = TerraformerOld.mc.getHeight(x, z)
            TerraformerOld.mc.setBlocks(x, minHeight, z, x2, modeY-1, z2, Block.DIRT)
            TerraformerOld.mc.setBlocks(x, modeY, z, x2, modeY, z2, Block.GRASS)
