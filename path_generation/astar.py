"""File for A* path finding algorithm
"""

import heapq
from environment.coord import Coord
from plots.plot import Plot

__author__ = "Jacob Eisho, Steven"


class AStarNode:
    """
    Defines a node for the AStar path finding algorithm
    """
    def __init__(self, coord, g, h, parent):
        """

        :param coord: Coord object
        :param g:
        :param h:
        :param parent: AStarNode object
        """
        self.coord = coord
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        """
        Returns True if self less than other
        :param other: AStarNode object
        :return: True or False
        """
        return self.f < other.f

    def __eq__(self, other):
        """
        Returns True if self equal to other
        :param other: AStarNode object
        :return: True or False
        """
        return self.coord == other.coord


def astar(plot: Plot(), start: Coord(), end: Coord()):
    """
    Returns a path from start to end containing only valid x, z coords
    :param plot: Plot object
    :param start: Coord object
    :param end: Coord object
    :return: A list of Coord
    """
    open_set = []
    closed_set = set()
    do_not_include = plot.pointsToIgnore
    start_node = AStarNode(start, 0, start.distance(end), None)
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.coord == end:
            path = []
            while current_node:
                path.append(current_node.coord)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.coord)

        subplot_points = {(coord.x, coord.z) for coord in do_not_include}
        for neighbour in current_node.coord.get_neighbours():

            if (neighbour.x, neighbour.z) not in subplot_points:

                if neighbour in closed_set:
                    continue

                g = current_node.g + current_node.coord.distance(neighbour)
                h = neighbour.distance(end)
                neighbour_node = AStarNode(neighbour, g, h, current_node)

                if neighbour_node in open_set:
                    existing_node = open_set[open_set.index(neighbour_node)]
                    if neighbour_node.g < existing_node.g:
                        existing_node.g = neighbour_node.g
                        existing_node.h = neighbour_node.h
                        existing_node.f = neighbour_node.f
                        existing_node.parent = neighbour_node.parent
                else:
                    heapq.heappush(open_set, neighbour_node)

    return None
