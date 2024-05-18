"""File for Terraformer class and terraforming logic
"""

import math
import mcpi.block as Block
from mcpi.minecraft import Minecraft
from environment.coord import Coord
from utils.settings import DEFAULT_SIGMA_S, DEFAULT_SIGMA_R

__author__ = "Jacob Eisho"


class Terraformer:
    """
    Terraformer static class
    """
    mc = Minecraft.create()

    @staticmethod
    def doTerraforming(plot):
        """
        Performs terraforming logic on input parameter
        :param plot: Plot abstract class
        :return: True if bilateral filtering successful, otherwise False
        """
        try:
            # Call Bilateral Filter helper method
            processedCoordsOfPlotPoints = Terraformer.bilateral_filter(plot, DEFAULT_SIGMA_S, DEFAULT_SIGMA_R)
            # Set the blocks
            for coord in processedCoordsOfPlotPoints:
                x, y, z = coord.x, coord.y, coord.z
                Terraformer.mc.setBlocks(x, 255, z, x, y, z, Block.AIR)
                Terraformer.mc.setBlocks(x, y-DEFAULT_SIGMA_S, z, x, y, z, Block.DIRT)
                Terraformer.mc.setBlock(x, y, z, Block.GRASS)
            # Update heights
            plot.start = Coord(plot.start.x, Terraformer.mc.getHeight(plot.start.x, plot.start.z), plot.start.z)
            plot.end = Coord(plot.end.x, Terraformer.mc.getHeight(plot.end.x, plot.end.z), plot.end.z)
            plot.refreshPoints()
            return True

        except ZeroDivisionError:
            print("Falling back to Circumferential Mode Filtering")
            return False

    @staticmethod
    def bilateral_filter(plot, sigma_s, sigma_r):
        """
        Performs bilateral filtering
        :param plot: Plot abstract class
        :param sigma_s: Sigma_Spatial, number of neighbouring blocks to consider in calculation
        :param sigma_r: Sigma_Range, range of y-levels to have in output
        :return: list of Coord objects that have had their y-levels bilaterally filtered
        """

        # Initialise lists of plot points
        coords = plot.points

        # Create a copy of the input coordinates to store the filtered output
        filtered_coords = [Coord(coord.x, coord.y, coord.z) for coord in coords]

        # Compute the square of the spatial smoothing parameter
        sigma_s_sq = sigma_s ** 2

        # Loop over each block in the plot
        for i in range(len(coords)):
            # Initialize the weighted sum and normalization factor
            weighted_sum = 0.0
            normalization = 0.0

            # Loop over the neighboring blocks within sigma_s
            for j in range(len(coords)):
                dist_sq = (coords[i].x - coords[j].x) ** 2 + (coords[i].y - coords[j].y) ** 2 + (
                        coords[i].z - coords[j].z) ** 2
                if dist_sq > sigma_s_sq:
                    continue

                # Compute the y-level weighting
                intensity_diff_sq = (coords[i].y - coords[j].y) ** 2
                weight = math.exp(-dist_sq / (2 * sigma_s_sq) - intensity_diff_sq / (2 * sigma_r ** 2))

                # Add the weighted value to the sum and the weight to the normalization factor
                weighted_sum += weight * coords[j].y
                normalization += weight

            # Normalize the weighted sum and assign the filtered y-level
            filtered_coords[i].y = weighted_sum / normalization

            # Keep track of the min and max y levels
            plot.minHeight = filtered_coords[i].y if filtered_coords[i].y < plot.minHeight else plot.minHeight
            plot.maxHeight = filtered_coords[i].y if filtered_coords[i].y > plot.maxHeight else plot.maxHeight
        return filtered_coords
