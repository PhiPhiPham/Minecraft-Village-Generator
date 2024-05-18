from mcpi import block as Block
"""THE FOLLOWING SETTINGS WILL CHANGE THE BEHAVIOUR OF OUR VILLAGE GENERATION ALGORITHMS"""

__author__ = "Jacob Eisho"

"""PLOT SIZES"""
DEFAULT_VILLAGE_PLOT_SIZE_X = 80
DEFAULT_VILLAGE_PLOT_SIZE_Z = 60
DEFAULT_BUILDING_PLOT_SIZE_X = 21
DEFAULT_BUILDING_PLOT_SIZE_Z = 21

"""TERRAFORMING FILTER SELECTION
1 = Multiple Circumferential Mode Filtering
2 = Single Circumferential Mode Filtering
3 = Bilateral Filtering (takes longest but looks the best)
"""
DEFAULT_TERRAFORM_ALGORITHM = 3

"""
MODIFIERS FOR MODE FILTER
Resolution for terrain smoothing
Bigger value may result in more natural terraforming but will take longer
"""
TERRAIN_SMOOTHING_MODIFIER = 0.3
DEFAULT_TERRAIN_SMOOTHING_RESOLUTION = int((DEFAULT_BUILDING_PLOT_SIZE_X + DEFAULT_BUILDING_PLOT_SIZE_Z) * TERRAIN_SMOOTHING_MODIFIER)

"""
MODIFIERS FOR BILATERAL FILTER
A larger SIGMA_S value means that more neighboring blocks are included when smoothing terrain.
A larger SIGMA_R value results in more extreme y-level smoothing.
"""
DEFAULT_SIGMA_S = 30
DEFAULT_SIGMA_R = 30

"""
VALID GROUND BLOCK IDS
Array of blocks we consider to be valid ground
"""
GROUND_BLOCKS = [Block.GRASS.id]

"""
MINIMUM DIMENSIONS FOR HOUSE 
"""
MIN_HOUSE_X = 19
MIN_HOUSE_Z = 19
