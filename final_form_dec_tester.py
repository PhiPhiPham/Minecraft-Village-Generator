# Assignment 1 main file
# Feel free to add additional modules/files as you see fit.

from mcpi.minecraft import Minecraft
from mcpi import block
from random import *
import random
import math

mc = Minecraft.create()
x, y, z = mc.player.getPos()

def place_items(x, y, z, length, width, item_list, num_stories):
    item_list = []
    item_list.append('table')
    item_list.append('couch')
    item_list.append('glowstone')
    item_list.append('flowerpot')
    item_list.append('overheadshelf')
    item_list.append('piano')
    
    for i in range(0,4):
                chosen_item = random.choice(item_list)
                if chosen_item == 'table':
                    # Placing tablea
                    create_table(x, y, z, length, width, num_stories)
                    item_list.remove('table')

                if chosen_item == 'couch':
                    # Placing couch
                    create_couch(x, y, z, length, width, num_stories)
                    item_list.remove('couch')
                if chosen_item == 'glowstone':
                    # Placing glowstone lamp
                    create_glowstone(x, y, z, length, width, num_stories)
                    item_list.remove('glowstone')
                if chosen_item == 'flowerpot':
                    # Placing flowerpot
                    create_flowerpot(x, y, z, length, width, num_stories)
                    item_list.remove('flowerpot')
                if chosen_item == 'overheadshelf':
                    create_overheadshelf(x, y, z, length, width, num_stories)
                    item_list.remove('overheadshelf')
                if chosen_item == 'piano':
                    # Placing piano
                    create_piano(x, y, z, length, width, num_stories)
                    item_list.remove('piano')



def create_small_room(x, y, z, length, width, displacement, height, num_stories):
    ## Length > Width of original rectangle
        air = 0
        mc.postToChat('length split')
        if length < width: 
            # Placing crafting table
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) , z + width - 1) == air:
               mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1, block.CRAFTING_TABLE)

            # Placing furnace
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1 - 1) == air:
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1), z + width - 1 - 1, block.FURNACE_ACTIVE.withData(5))

            # Placing chest
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1 - 1 - 1) == air:
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1 - 1 - 1, block.CHEST.withData(5))
            

            # Placing bed 
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + 1) == air: 
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + 1, block.BED.withData(10)) 
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + 1 + 1, block.BED.withData(2)) 
            
            # Placing wallshelf
            create_wallshelf(x, y, z, length, width, displacement, num_stories)
        

        # Randomly place table

        # Width > Length of original rectangle
        else:
            mc.postToChat('width split')
            # Placing crafting table
            if mc.getBlock(x + 5 + 1 , y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement)) == air:
                mc.setBlock(x + 5 + 1 , y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.CRAFTING_TABLE)

            # Placing furnace
            if mc.getBlock(x + 5 + 1 + 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement)) == air:
                mc.setBlock(x + 5 + 1 + 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.FURNACE_ACTIVE)

            # Placing chest 
            if mc.getBlock(x + 5 + 1 + 1 + 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement)) == air:
                mc.setBlock(x + 5 + 1 + 1 + 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.CHEST)
            

            # Placing bed 
            if mc.getBlock(x + 5 + length - 1 - 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement)) == air:
                mc.setBlock(x + 5 + length - 1 - 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.BED.withData(9))
                mc.setBlock(x + 5 + length - 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.BED.withData(1))

            # Placing wallshelf
            create_wallshelf(x, y, z, length, width, displacement, num_stories)
                
           
            

def create_big_room(x, y, z, length, width, displacement, height, num_stories):    
    ## Length > Width of original rectangle
        air = 0
        mc.postToChat('length split')
        if length < width: 
            # Placing crafting table
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1) == air:
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1, block.CRAFTING_TABLE)

            # Placing furnace
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1 - 1) == air:
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1 - 1, block.FURNACE_ACTIVE.withData(5))

            # Placing chest
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1 - 1 - 1) == air:
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + width - 1 - 1 - 1, block.CHEST.withData(5))
            

            # Placing bed 
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + 1) == air: 
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + 1, block.BED.withData(10)) 
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1), z + 1 + 1, block.BED.withData(2)) 
            
            create_wallshelf(x, y, z, length, width, displacement, num_stories)
    
        

        # Randomly place table

        # Width > Length of original rectangle
        else:
            mc.postToChat('width split')
            # Placing crafting table
            if mc.getBlock(x + 5 + 1 , y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement)) == air:
                mc.setBlock(x + 5 + 1 , y + + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.CRAFTING_TABLE)

            # Placing furnace
            if mc.getBlock(x + 5 + 1 + 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement)) == air:
                mc.setBlock(x + 5 + 1 + 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.FURNACE_ACTIVE)

            # Placing chest 
            if mc.getBlock(x + 5 + 1 + 1 + 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement)) == air:
                mc.setBlock(x + 5 + 1 + 1 + 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.CHEST)
            

            # Placing bed 
            if mc.getBlock(x + 5 + length - 1 - 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement)) == air:
                mc.setBlock(x + 5 + length - 1 - 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.BED.withData(9))
                mc.setBlock(x + 5 + length - 1, y + height * (num_stories - 1) + (num_stories - 1), z + width + (1 * displacement), block.BED.withData(1))
            
            create_wallshelf(x, y, z, length, width, displacement, num_stories)

            
# Block Palette 1
light_wood = 5
medium_wood = 17
# Randomly set length, width and height of house
length = random.randint(15, 20)
height = 4
width = random.randint(15, 20)

# Generate the walls
mc.setBlocks(x + 5, y, z, x + 5 + length, y + height, z + width, block.STONE_BRICK)

# Hollow out block
mc.setBlocks(x + 6, y, z + 1, x + 5 + length - 1, y + height, z + width - 1, block.AIR)

# Generate the floors
mc.setBlocks(x + 5, y - 1, z, x + 5 + length, y - 1, z + width, block.WOOD_PLANKS)

# Generate windows
# Left side of the house
mc.setBlocks(x + 5 + 2, y + 1, z, x + 5 + length - 2, y + height - 2, z, block.GLASS)

# Right side of the house
mc.setBlocks(x + 5 + 2, y + 1, z + width, x + 5 + length - 2, y + height - 2, z + width, block.GLASS)

# Front side of the house
mc.setBlocks(x + 5, y + 1, z + 2, x + 5, y + height - 2, z + width - 2, block.GLASS)

# Back side of the house
mc.setBlocks(x + 5 + length, y + 1, z + 2, x + 5 + length, y + height - 2, z + width - 2, block.GLASS)




def create_table(x, y, z, length, width, num_stories):
    # Placing tables
    air = 0
    timeout = 0
    random_l = randint(0, length)
    random_w = randint(0, width)
    # Length > Width for orginal
    while (mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w) != air) or (mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w) != air) or mc.getBlock(x + 5 + random_l,y + height * (num_stories - 1) + (num_stories - 1), z + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w) != air:
        random_l = randint(0, length)
        random_w = randint(0, width)
        timeout += 1
        if timeout == 10:
            mc.postToChat('not working')
            return True
    
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w, block.STAIRS_COBBLESTONE.withData(5))
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w, block.STAIRS_COBBLESTONE.withData(5))
    mc.setBlock(x + 5 + random_l,y + height * (num_stories - 1) + (num_stories - 1), z + random_w, block.STAIRS_COBBLESTONE.withData(4))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w, block.STAIRS_COBBLESTONE.withData(4))

def create_couch(x, y, z, length, width, num_stories):
    air = 0
    random_l = randint(0, length)
    random_w = randint(0, width)
    wool_colour = randint(0,15)
    timeout = 0
    # Length > Width for orginal
    while (mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z - 1 + random_w) != air) or (mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 3 + random_w) != air) or mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w) != air or mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z - 1 + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 3 + random_w) != air or mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 2 + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 2 + random_w) != air:
        random_l = randint(0, length)
        random_w = randint(0, width)
        timeout += 1
        if timeout == 10:
            return True
         
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z - 1 + random_w, block.STAIRS_STONE_BRICK.withData(6))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z - 1 + random_w, block.STAIRS_STONE_BRICK.withData(6))
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 3 + random_w, block.STAIRS_STONE_BRICK.withData(7))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 3 + random_w, block.STAIRS_STONE_BRICK.withData(7))
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w, block.WOOL.withData(wool_colour))
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w, block.WOOL.withData(wool_colour))
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 2 + random_w, block.WOOL.withData(wool_colour))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w, block.STONE_SLAB)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w, block.STONE_SLAB)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 2 + random_w, block.STONE_SLAB)


def create_glowstone(x, y, z, length, width, num_stories):
    random_l = randint(0, length)
    random_w = randint(0, width)
    air = 0
    timeout = 0
    # Length > Width for orginal
    while mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + random_w) != air:
        random_l = randint(0, length)
        random_w = randint(0, width)
        timeout += 1
        if timeout == 10:
            mc.postToChat("can't find")
            return True 
    
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + random_w, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + random_w, block.FENCE)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + random_w, block.FENCE)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w, block.FENCE)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) - 1, z + random_w, block.WOOD)

def create_flowerpot(x, y, z, length, width, num_stories):
    random_l = randint(0, length)
    random_w = randint(0, width)
    flower = randint(0,8)
    air = 0
    timeout = 0
    while mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w) != air or mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w) != air or mc.getBlock(x + 5 + 2 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w) != air or mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z - 1 + random_w) != air:
        random_l = randint(0, length)
        random_w = randint(0, width)
        timeout += 1
        if timeout == 10:
            return True 
    
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w, block.GRASS)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w, block.TRAPDOOR.withData(6))
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w, block.TRAPDOOR.withData(5))
    mc.setBlock(x + 5 + 2 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + random_w, block.TRAPDOOR.withData(7))
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z - 1 + random_w, block.TRAPDOOR.withData(4))
    mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + random_w, block.FLOWER_CYAN.withData(flower))
    
def create_overheadshelf(x, y, z, length, width, num_stories):
    random_l = randint(0, length)
    random_w = randint(0, width)
    air = 0
    timeout = 0
    # Length > Width for orginal
     
    slab_colour = randint(8,13)
    while mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + 3 + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 1 + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 2 + random_w) != air:
        random_l = randint(0, length)
        random_w = randint(0, width)
        timeout += 1
        if timeout == 10:
            return True
        
    # handles
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + random_w, block.FENCE)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + 3 + random_w, block.FENCE)

    # slabs
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + random_w, block.WOODEN_SLAB.withData(slab_colour))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 1 + random_w, block.WOODEN_SLAB.withData(slab_colour))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 2 + random_w, block.WOODEN_SLAB.withData(slab_colour))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 3 + random_w, block.WOODEN_SLAB.withData(slab_colour))

    # chest 
    ender_chest = 130
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + 1 + random_w, block.CHEST.withData(4))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + 2 + random_w, ender_chest, 5)
        



def create_wallshelf(x, y, z, length, width, displacement, num_stories):
    air = 0
    slab_colour = randint(8,13)
    random_l = randint(0, length - 2)
    random_w = randint(0, width - 2)
    if length < width: ## Length > Width of original rectangle 
            # Placing Shelves
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + random_w) == air and mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 2 + random_w) == air:
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + random_w, block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 1 + random_w , block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 2 + random_w , block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 3, z + random_w , 84)
    
    else: ## Width > Length of original rectangle 
        if mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement)) == air and mc.getBlock(x + 5 + 2 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement)) == air:
                mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement), block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement), block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + 2 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement), block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + width + (1 * displacement), 84)

def create_piano(x, y, z, length, width, num_stories):
    random_l = randint(0, length)
    random_w = randint(0, width)
    stone_pressurep = 70
    jukebox = 84
    air = 0
    timeout = 0
    
    while mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + 4 + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 1 + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 3 + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 2 + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + 2 + random_w) != air:
        random_l = randint(0, length)
        random_w = randint(0, width)
        timeout += 1
        if timeout == 10:
            return True
    
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w, block.STAIRS_NETHER_BRICK.withData(4))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 2 + random_w, block.STAIRS_NETHER_BRICK.withData(4))
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 3 + random_w, block.STAIRS_NETHER_BRICK.withData(4))

    # The keys
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 1 + random_w, stone_pressurep)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 2 + random_w, stone_pressurep)
    mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 3 + random_w, stone_pressurep)

    # The body
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 1 + random_w, jukebox)
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + 2 + random_w, jukebox)
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 2 + random_w, jukebox)
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + 3 + random_w, jukebox)
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 3 + random_w, jukebox)
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + 1 + random_w, jukebox)

    # Fancy sides: Left
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + random_w, block.TRAPDOOR.withData(4))
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + random_w, block.TRAPDOOR.withData(4))

    #Fancy sides: Right
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + 4 + random_w, block.TRAPDOOR.withData(5))
    mc.setBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 4 + random_w, block.TRAPDOOR.withData(5))

        
    
item_list = []
item_list.append('table')
item_list.append('couch')
# item_list.append('glowstone')
# item_list.append('flowerpot')
# item_list.append('overheadshelf')
# item_list.append('piano')        

# Generate door
# Chooses which wall will have the door
door_flag_east = False
door_flag_west = False
door_flag_south = False
door_flag_north = False

choose_wall = random.randint(1, 2)
if choose_wall == 1:
    wall = random.randint(1, 2)
    set_door = length // 2
    if wall == 1: # East
        mc.setBlocks(x + 5 + set_door - 1, y, z, x + 5 + set_door + 1, y + 3, z, block.STONE_BRICK)
        mc.setBlock(x + 5 + set_door, y + 1, z, 64, 8)
        mc.setBlock(x + 5 + set_door, y, z, 64, 1)
        door_flag_east = True

    elif wall == 2: # West
        mc.setBlocks(x + 5 + set_door - 1, y, z + width, x + 5 + set_door + 1, y + 3, z + width, block.STONE_BRICK)
        mc.setBlock(x + 5 + set_door, y + 1, z + width, 64, 8)
        mc.setBlock(x + 5 + set_door, y, z + width, 64, 0)
        door_flag_west = True

else: 
    wall = random.randint(1, 2)
    set_door = width // 2
    if wall == 1: # South
        mc.setBlocks(x + 5, y, z + set_door - 1, x + 5, y + 3, z + set_door + 1, block.STONE_BRICK)
        mc.setBlock(x + 5, y + 1, z + set_door, 64, 8)
        mc.setBlock(x + 5, y, z + set_door, 64, 0)
        door_flag_south = True
    
    elif wall == 2: # North
        mc.setBlocks(x + 5 + length, y, z + set_door - 1, x + 5 + length, y + 3, z + set_door + 1, block.STONE_BRICK)
        mc.setBlock(x + 5 + length, y + 1, z + set_door, 64, 9)
        mc.setBlock(x + 5 + length, y, z + set_door, 64, 7)
        door_flag_north = True

# Placing bookshelf stair wall
# The door is east or west
if door_flag_west == True:
        shelf_wall = [4]
        door_wall = 1
if door_flag_north == True:
        shelf_wall = [4]
        door_wall = 2
if door_flag_east == True:
        shelf_wall = [4]
        door_wall = 3
if door_flag_south == True:
        shelf_wall = [4]
        door_wall = 4

chosen_wall = random.choice(shelf_wall)
if chosen_wall == 1:
    # West
    # Shelves
    mc.setBlocks(x + 5 + 1, y, z + 1, x + 5 + length - 1, y + 3, z + 1, block.BOOKSHELF)
    mc.setBlocks(x + 5 + 1 + 1, y + 1, z + 1, x + 5 + length - 1 - 1, y + 2, z + 1, block.AIR)
    mc.setBlocks(x + 5 + 1, y, z + 2, x + 5 + length - 1, y, z + 2  , block.STAIRS_WOOD.withData(3))


elif chosen_wall == 3: # East
    
    mc.setBlocks(x + 5 + 1, y, z + width - 1, x + 5 + length - 1, y + 3, z + width - 1, block.BOOKSHELF)
    mc.setBlocks(x + 5 + 1 + 1, y + 1, z + width - 1, x + 5 + length - 1 - 1, y + 2, z + width - 1, block.AIR)
    mc.setBlocks(x + 5 + 1, y, z + width - 2, x + 5 + length - 1, y, z + width - 2, block.STAIRS_WOOD.withData(2))

elif chosen_wall == 2: # North
    mc.setBlocks(x + 5 + length - 1, y, z + 1, x + 5 + length - 1, y + 3, z + width - 1, block.BOOKSHELF)
    mc.setBlocks(x + 5 + length - 1, y + 1, z + 1 + 1, x + 5 + length - 1, y + 2, z + width - 1 - 1, block.AIR)
    mc.setBlocks(x + 5 + length - 1 - 1, y, z + 1, x + 5 + length - 1 - 1, y, z + width - 1, block.STAIRS_WOOD.withData(0))
    
elif chosen_wall == 4: # South
    mc.setBlocks(x + 5 + 1, y, z + 1, x + 5 + 1, y + 3, z + width - 1, block.BOOKSHELF)
    mc.setBlocks(x + 5 + 1, y + 1, z + 1 + 1, x + 5 + 1, y + 2, z + width - 1 - 1, block.AIR)
    mc.setBlocks(x + 5 + 1 + 1, y, z + 1, x + 5 + 1 + 1, y, z + width - 1, block.STAIRS_WOOD.withData(1))

if door_wall != 1:
    # West
    flower = randint(0,7)
    mc.setBlocks(x + 5 + 2, y, z + width + 1, x + 5 + length - 2, y, z + width + 1, block.GRASS)
    mc.setBlocks(x + 5 + 2, y + 1, z + width + 1, x + 5 + length - 2, y + 1, z + width + 1, block.FLOWER_CYAN.withData(flower))


if door_wall != 3: # East
    # Left side of the house 
    flower = randint(0,7)
    mc.setBlocks(x + 5 + 2, y, z - 1, x + 5 + length - 2, y, z - 1, block.GRASS)
    mc.setBlocks(x + 5 + 2, y + 1, z - 1, x + 5 + length - 2, y + 1, z - 1, block.FLOWER_CYAN.withData(flower))
    # mc.setBlocks(x + 5 + 2, y, z - 2, x + 5 + length - 2, y, z - 2, block.TRAPDOOR.withData(4))
    # mc.setBlock(x + 5 + 1, y, z - 1, block.TRAPDOOR.withData(6))
    
    # Right side of the house
if door_wall != 2: # North
    # Back side of the house
    flower = randint(0,7)
    mc.setBlocks(x + 5 + length + 1, y, z + 2, x + 5 + length + 1, y, z + width - 2, block.GRASS)
    mc.setBlocks(x + 5 + length + 1, y + 1, z + 2, x + 5 + length + 1, y + 1, z + width - 2, block.FLOWER_CYAN.withData(flower))
    
if door_wall != 4: # South
    flower = randint(0,7)
    # Front side of the house
    mc.setBlocks(x + 4, y, z + 2, x + 4, y, z + width - 2, block.GRASS)
    mc.setBlocks(x + 4, y + 1, z + 2, x + 4, y + 1, z + width - 2, block.FLOWER_CYAN.withData(flower))
    

# Roof design 1
def roof_design_1(num_stories):
    roof_start = height * num_stories + (num_stories - 1)
    min_size = min(length, width) // 3
    for i in range(0, min_size):
        mc.setBlocks(x + 4 + i, y + roof_start + i, z - 1 + i, x + 6 + length - i, y + roof_start + i, z - 1 + i, 164, 2)
        mc.setBlocks(x + 4 + i, y + roof_start + i, z + width + 1 - i, x + 6 + length - i, y + roof_start + i, z + width + 1 - i, 164, 3)
        mc.setBlocks(x + 4 + i, y + roof_start + i, z + i, x + 4 + i, y + roof_start + i, z + width - i, 164, 0)
        mc.setBlocks(x + 6 + length - i, y + roof_start + i, z + i, x + 6 + length - i, y + roof_start + i, z + width - i, 164, 1)

        if i == min_size - 1:
            mc.setBlocks(x + 4 + i + 1, y + roof_start + i, z - 1 + i + 1, x + 6 + length - i - 1, y + roof_start + i, z + width - i, 5, 5)

# Roof design 3
def roof_design_3(num_stories):
    i = num_stories - 1
    j = num_stories - 2

    mc.setBlocks(x + 4, y - 1, z - 1, x + 4, y + (height * num_stories) + num_stories, z - 1, 17, 12)
    mc.setBlocks(x + 5 + length + 1, y - 1, z - 1, x + 5 + length + 1, y + (height * num_stories) + num_stories, z - 1, 17, 12)
    mc.setBlocks(x + 4, y - 1, z + width + 1, x + 4, y + (height * num_stories) + num_stories, z + width + 1, 17, 12)
    mc.setBlocks(x + 5 + length + 1, y - 1, z + width + 1, x + 5 + length + 1, y + (height * num_stories) + num_stories, z + width + 1, 17, 12)

    if num_stories > 1:
        for k in range(num_stories):
            mc.setBlocks(x + 4, y + (height * i) + j, z - 1, x + 4, y + (height * i) + j, z + width + 1, 17, 12)
            mc.setBlocks(x + 5 + length + 1, y + (height * i) + j, z - 1, x + 5 + length + 1, y + (height * i) + j, z + width + 1, 17, 12)
            mc.setBlocks(x + 4, y + (height * i) + j, z - 1, x + 5 + length + 1, y + (height * i) + j, z - 1, 17, 12)
            mc.setBlocks(x + 4, y + (height * i) + j, z + width + 1, x + 5 + length + 1, y + (height * i) + j, z + width + 1, 17, 12)

            i += 1
            j += 2
    else:
        mc.setBlocks(x + 4, y + height + 1, z - 1, x + 4, y + height + 1, z + width + 1, 17, 12)
        mc.setBlocks(x + 5 + length + 1, y + height + 1, z - 1, x + 5 + length + 1, y + height + 1, z + width + 1, 17, 12)
        mc.setBlocks(x + 4, y + height + 1, z - 1, x + 5 + length + 1, y + height + 1, z - 1, 17, 12)
        mc.setBlocks(x + 4, y + height + 1, z + width + 1, x + 5 + length + 1, y + height + 1, z + width + 1, 17, 12)

# Recursive algorithm to generate rooms
def generate_rooms(x, y, z, length, width, height, num_stories):
    # Stops generating rooms if the length/width reaches 4 blocks
    if length <= 6 or width <= 6:
        return -1
    else:
        if length >= width:
            # Places a wall near the midpoint of the house/room
            room_midpoint = length // 2
            wall_place_list = [room_midpoint - 2, room_midpoint + 2]
            place_wall = random.choice(wall_place_list)
            mc.setBlocks(x + 5 + place_wall, y + height * (num_stories - 1), z, x + 5 + place_wall, y + height * num_stories, z + width, block.STONE_BRICK)
            
            # Add doorway
            mc.setBlocks(x + 5 + place_wall, y + (height * (num_stories - 1)) + (num_stories - 1), z + width // 2, x + 5 + place_wall, y + (height * (num_stories - 1)) + num_stories, z + width // 2, block.AIR)
            
            
            positive_room = 1
            negative_room = -1

            # Places items into the bottom half because it is a bigger room
            if place_wall > room_midpoint:
                create_big_room(x, y, z, place_wall, width, negative_room, height, num_stories)
            # Places items into the top half because it is a bigger
            else:
                create_big_room(x, y, z, place_wall, width, positive_room, height, num_stories)
                    
            # 1/2 chance to generate another room
            room_chance = random.randint(1, 2)
            if room_chance == 2:
                generate_rooms(x, y, z, place_wall, width, height, num_stories)
            else: # This is to generate the second room 
                # Places items into the top half because it is a smaller room
                if place_wall > room_midpoint:
                    create_small_room(x, y, z, place_wall, width, positive_room, height, num_stories)

                else: # Places items into the bottom half because it is a smaller 
                    create_small_room(x, y, z, place_wall, width, negative_room, height, num_stories)
            


        elif width > length:
            room_midpoint = width // 2
            wall_place_list = [room_midpoint - 2, room_midpoint + 2]
            place_wall = random.choice(wall_place_list)        
            mc.setBlocks(x + 5, y + height * (num_stories - 1), z + place_wall, x + 5 + length, y + height * num_stories, z + place_wall, block.STONE_BRICK)
            
            # Add a doorway
            mc.setBlocks(x + 5 + length // 2, y + (height * (num_stories - 1)) + (num_stories - 1), z + place_wall, x + 5 + length // 2, y + (height * (num_stories - 1)) + num_stories, z + place_wall, block.AIR)

            positive_room = 1
            negative_room = -1
            
            # Places items into the left half because it is a bigger room
            if place_wall > room_midpoint:
                create_big_room(x, y, z, length, place_wall, negative_room, height, num_stories)
            # Places items into the right half because it is a bigger
            else:
                create_big_room(x, y, z, length, place_wall, positive_room, height, num_stories)
            
            # 1/2 chance to generate another room
            room_chance = random.randint(1, 2)
            if room_chance == 2:
                generate_rooms(x, y, z, length, place_wall, height, num_stories)
            else: # This is to generate the second room 
                # Places items into the right half because it is a smaller room
                if place_wall > room_midpoint:
                    create_small_room(x, y, z, length, place_wall, positive_room, height, num_stories)
                # Places items into the left half because it is a smaller 
                else:
                    create_small_room(x, y, z, length, place_wall, negative_room, height, num_stories)
            
            # place items into the rooms

generate_rooms(x, y, z, length, width, height, 1)

# Generate staircase if num_stories > 1
def generate_stairs():
    pass

# Generate random number of stories for the house
num_stories = random.randint(2, 2)
place_items(x, y, z, length, width, height, 1)


if num_stories == 1:
    # choose_roof = random.randint(1, 2)
    # if choose_roof == 1:
    #     roof_design_1(num_stories)
    # else:
    #     roof_design_3(num_stories)
    pass
else:
    i = 1
    j = 2
    k = 0

    while i < num_stories:
        # Generate the walls
        mc.setBlocks(x + 5, y + height * i + i, z, x + 5 + length, y + height * j + i, z + width, block.STONE_BRICK)
        mc.setBlocks(x + 6, y + height * i, z + 1, x + 5 + length - 1, y + height * j + k, z + width - 1, block.AIR)

        # Generate windows
        mc.setBlocks(x + 5 + 2, y + height * i + i + 1, z, x + 5 + length - 2, y + height * j + i - 2, z, block.GLASS)
        mc.setBlocks(x + 5 + 2, y + height * i + i + 1, z + width, x + 5 + length - 2, y + height * j + i - 2, z + width, block.GLASS)
        mc.setBlocks(x + 5, y + height * i + i + 1, z + 2, x + 5, y + height * j + i - 2, z + width - 2, block.GLASS)
        mc.setBlocks(x + 5 + length, y + height * i + i + 1, z + 2, x + 5 + length, y + height * j + i - 2, z + width - 2, block.GLASS)

        # Generate rooms for the floor
        generate_rooms(x, y, z, length, width, height, num_stories)

        place_items(x, y, z, length, width, item_list, num_stories)

        # Generate the floors
        mc.setBlocks(x + 6, y + height * i + k, z + 1, x + 5 + length - 1, y + height * i + k, z + width - 1, block.WOOD_PLANKS)

        i += 1
        j += 1
        k += 1

    # choose_roof = random.randint(1, 2)
    # if choose_roof == 1:
    #     roof_design_1(num_stories)
    # else:
    #     roof_design_3(num_stories)

    

    