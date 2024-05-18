"""Driver code for Minecraft village generation.
"""

import random
from helpers.misc import Misc
from environment.coord import Coord
from plots.builder import Builder
from plots.house_plot import HousePlot
from plots.village_plot import VillagePlot
from utils.settings import DEFAULT_BUILDING_PLOT_SIZE_X, DEFAULT_BUILDING_PLOT_SIZE_Z, DEFAULT_VILLAGE_PLOT_SIZE_X, \
    DEFAULT_VILLAGE_PLOT_SIZE_Z, MIN_HOUSE_X, MIN_HOUSE_Z
from path_generation.astar import astar

__author__ = "Jacob Eisho"

"""INITIALISE MCPI"""
x, y, z = Misc.playerCoords()

"""GET PLOT DIMS BASED ON PLAYER POS"""
y = Misc.getHeight(x - (DEFAULT_VILLAGE_PLOT_SIZE_X // 2), z - (DEFAULT_VILLAGE_PLOT_SIZE_Z // 2))
start = Coord(x - (DEFAULT_VILLAGE_PLOT_SIZE_X // 2), y, z - (DEFAULT_VILLAGE_PLOT_SIZE_Z // 2))
y = Misc.getHeight(x + (DEFAULT_VILLAGE_PLOT_SIZE_X // 2), z + (DEFAULT_VILLAGE_PLOT_SIZE_Z // 2))
end = Coord(x + (DEFAULT_VILLAGE_PLOT_SIZE_X // 2), y, z + (DEFAULT_VILLAGE_PLOT_SIZE_Z // 2))

"""VILLAGE PLOT"""
village_plot = VillagePlot(start, end)
v_builder = Builder(village_plot)

"""BUILD VILLAGE"""
numOfPlotsToCreate = 5
i = 0
doorCoords = []
while i < numOfPlotsToCreate:
    subp_start = Coord(random.randint(start.x, end.x), random.randint(start.z, end.z), random.randint(start.z, end.z))
    x_modifier = random.randint(MIN_HOUSE_X, DEFAULT_BUILDING_PLOT_SIZE_X)
    z_modifier = random.randint(MIN_HOUSE_Z, DEFAULT_BUILDING_PLOT_SIZE_Z)
    subp_end = Coord(subp_start.x + x_modifier, subp_start.y, subp_start.z + z_modifier)
    # Ensure start and end are not in another plot
    if i == 0:
        subp = HousePlot(subp_start, subp_end)
        subp.terraform()
        village_plot.addSubPlot(subp)
        subp_builder = Builder(subp)
        subp_builder.buildHouse()
        doorCoords.append(subp_builder.door_coords)
        i += 1
    else:
        subp = HousePlot(subp_start, subp_end)
        perimeter = subp.getPerimeter()
        subp_points_x = {coord.x for coord in perimeter}
        subp_points_z = {coord.z for coord in perimeter}
        build = True
        for subplot in village_plot.sub_plots:
            subplot_points_x = {coord.x for coord in subplot.points}
            subplot_points_z = {coord.z for coord in subplot.points}
            if (subp_points_x & subplot_points_x) and (subp_points_z & subplot_points_z):
                build = False
                break
        if build:
            subp.terraform()
            village_plot.addSubPlot(subp)
            subp_builder = Builder(subp)
            subp_builder.buildHouse()
            doorCoords.append(subp_builder.door_coords)
            i += 1

"""BUILD PATHS"""
village_plot.refreshPoints()
v_points = village_plot.points
for i in range(1, len(doorCoords)):
    path = astar(village_plot, doorCoords[i-1], doorCoords[i])
    if path:
        for p_coord in path:
            ptest = [(coord.x, coord.y, coord.z) for coord in v_points if coord.x == p_coord.x and coord.z == p_coord.z]
            if ptest:
                x, y, z = ptest[0]
                Misc.setBlock(x, y, z, 1)
