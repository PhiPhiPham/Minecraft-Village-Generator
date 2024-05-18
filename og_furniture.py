from mcpi.minecraft import Minecraft
from mcpi import block
from random import *
import random
import math

mc = Minecraft.create()
x, y, z = mc.player.getPos()

# Table
# mc.setBlock(x + 3 + 2, y, z, block.STAIRS_WOOD.withData(5))
# mc.setBlock(x + 3 + 2, y, z + 1, block.STAIRS_WOOD.withData(5))
# mc.setBlock(x + 3 + 1,y, z, block.STAIRS_WOOD.withData(4))
# mc.setBlock(x + 3 + 1, y, z + 1, block.STAIRS_WOOD.withData(4))

#couch

# for i in range(0, 15): 
#     mc.setBlock(x + 3 + 1 + (i * 3), y, z - 1, block.STAIRS_STONE_BRICK.withData(6))
#     mc.setBlock(x + 3 + (i * 3), y, z - 1, block.STAIRS_STONE_BRICK.withData(6))
#     mc.setBlock(x + 3 + 1 + (i * 3), y, z + 3, block.STAIRS_STONE_BRICK.withData(7))
#     mc.setBlock(x + 3 + (i * 3), y, z + 3, block.STAIRS_STONE_BRICK.withData(7))
#     mc.setBlock(x + 3 + 1 + (i * 3), y, z, block.WOOL.withData(i))
#     mc.setBlock(x + 3 + 1 + (i * 3), y, z + 1, block.WOOL.withData(i))
#     mc.setBlock(x + 3 + 1 + (i * 3), y, z + 2, block.WOOL.withData(i))
#     mc.setBlock(x + 3 + (i * 3), y, z, block.STONE_SLAB)
#     mc.setBlock(x + 3 + (i * 3), y, z + 1, block.STONE_SLAB)
#     mc.setBlock(x + 3 + (i * 3), y, z + 2, block.STONE_SLAB)

# Glowstone
# mc.setBlock(x + 3, y + 3, z, block.GLOWSTONE_BLOCK)
# mc.setBlock(x + 3, y + 2, z, block.FENCE)
# mc.setBlock(x + 3, y + 1, z, block.FENCE)
# mc.setBlock(x + 3, y, z, block.FENCE)
# mc.setBlock(x + 3, y - 1, z, block.WOOD)

# for i in range(0,8):
#     mc.setBlock(x + 5 + 1 + i * 3, y, z, block.GRASS)
#     mc.setBlock(x + 5 + i * 3, y, z, block.TRAPDOOR.withData(6))
#     mc.setBlock(x + 5 + 1 + i * 3, y, z + 1, block.TRAPDOOR.withData(5))
#     mc.setBlock(x + 5 + 2 + i * 3, y, z, block.TRAPDOOR.withData(7))
#     mc.setBlock(x + 5 + 1 + i * 3, y, z - 1, block.TRAPDOOR.withData(4))
#     mc.setBlock(x + 5 + 1 + i * 3, y + 1, z, block.FLOWER_CYAN.withData(i))

# Overhead shelf
# for i in range(0,5):
#     # handles
#     mc.setBlock(x + 3 + (i * 2), y + 3, z, block.FENCE)
#     mc.setBlock(x + 3 + (i * 2), y + 3, z + 3, block.FENCE)

#     # slabs
#     mc.setBlock(x + 3 + (i * 2), y + 2, z, block.WOODEN_SLAB.withData(i + 8))
#     mc.setBlock(x + 3 + (i * 2), y + 2, z + 1, block.WOODEN_SLAB.withData(i + 8))
#     mc.setBlock(x + 3 + (i * 2), y + 2, z + 2, block.WOODEN_SLAB.withData(i + 8))
#     mc.setBlock(x + 3 + (i * 2), y + 2, z + 3, block.WOODEN_SLAB.withData(i + 8))

#     # chest 
#     ender_chest = 130
#     mc.setBlock(x + 3 + (i * 2), y + 3, z + 1, block.CHEST.withData(4))
#     mc.setBlock(x + 3 + (i * 2), y + 3, z + 2, ender_chest, 5)

# Wall shelf
 
# mc.setBlock(x + 3, y + 2, z, block.WOODEN_SLAB.withData(8))
# mc.setBlock(x + 3, y + 2, z + 1 , block.WOODEN_SLAB.withData(8))
# mc.setBlock(x + 3, y + 2, z + 2 , block.WOODEN_SLAB.withData(8))
# mc.setBlock(x + 3, y + 3, z , 84)

# Piano
# stone_pressurep = 70
# jukebox = 84

# mc.setBlock(x + 3, y, z + 1, block.STAIRS_NETHER_BRICK.withData(4))
# mc.setBlock(x + 3, y, z + 2, block.STAIRS_NETHER_BRICK.withData(4))
# mc.setBlock(x + 3, y, z + 3, block.STAIRS_NETHER_BRICK.withData(4))

# # The keys
# mc.setBlock(x + 3, y + 1, z + 1, stone_pressurep)
# mc.setBlock(x + 3, y + 1, z + 2, stone_pressurep)
# mc.setBlock(x + 3, y + 1, z + 3, stone_pressurep)

# # The body
# mc.setBlock(x + 3 + 1, y + 1, z + 1, jukebox)
# mc.setBlock(x + 3 + 1, y, z + 2, jukebox)
# mc.setBlock(x + 3 + 1, y + 1, z + 2, jukebox)
# mc.setBlock(x + 3 + 1, y, z + 3, jukebox)
# mc.setBlock(x + 3 + 1, y + 1, z + 3, jukebox)
# mc.setBlock(x + 3 + 1, y, z + 1, jukebox)

# # Fancy sides: Left
# mc.setBlock(x + 3 + 1, y, z, block.TRAPDOOR.withData(4))
# mc.setBlock(x + 3 + 1, y + 1, z, block.TRAPDOOR.withData(4))

# #Fancy sides: Right
# mc.setBlock(x + 3 + 1, y, z + 4, block.TRAPDOOR.withData(5))
# mc.setBlock(x + 3 + 1, y + 1, z + 4, block.TRAPDOOR.withData(5))

mc.setBlocks(x, y, z, x + 15, y + 6, z + 15, block.AIR)