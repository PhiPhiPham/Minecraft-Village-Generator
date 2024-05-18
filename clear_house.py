from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
x, y, z = mc.player.getPos()

mc.setBlocks(x + 3, y, z, x + 5 + 25, y + 20, z + 25, block.AIR)
mc.setBlocks(x + 3, y - 1, z, x + 25, y - 1, z + 25, 2)