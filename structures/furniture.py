from mcpi.minecraft import Minecraft
from mcpi import block
from random import *
import random

mc = Minecraft.create()
x, y, z = mc.player.getPos()

def place_items(x, y, z, length, width, height, num_stories):
    item_list = []
    item_list.append('table')
    item_list.append('couch')
    item_list.append('glowstone')
    item_list.append('flowerpot')
    item_list.append('overheadshelf')
    item_list.append('piano')
    
    for i in range(0, 4):
                chosen_item = random.choice(item_list)
                if chosen_item == 'table':
                    # Placing tablea
                    create_table(x, y, z, length, width, height, num_stories)
                    item_list.remove('table')

                if chosen_item == 'couch':
                    # Placing couch
                    create_couch(x, y, z, length, width, height,  num_stories)
                    item_list.remove('couch')
                if chosen_item == 'glowstone':
                    # Placing glowstone lamp
                    create_glowstone(x, y, z, length, width, height, num_stories)
                    item_list.remove('glowstone')
                if chosen_item == 'flowerpot':
                    # Placing flowerpot
                    create_flowerpot(x, y, z, length, width, height, num_stories)
                    item_list.remove('flowerpot')
                if chosen_item == 'overheadshelf':
                    create_overheadshelf(x, y, z, length, width, height,  num_stories)
                    item_list.remove('overheadshelf')
                if chosen_item == 'piano':
                    # Placing piano
                    create_piano(x, y, z, length, width, height, num_stories)
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
            create_wallshelf(x, y, z, length, width, displacement, height, num_stories)
        

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
            create_wallshelf(x, y, z, length, width, displacement, height, num_stories)
                
           
            

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
            
            create_wallshelf(x, y, z, length, width, displacement, height, num_stories)
    
        

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
            
            create_wallshelf(x, y, z, length, width, displacement, height, num_stories)

def create_table(x, y, z, length, width, height, num_stories):
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

def create_couch(x, y, z, length, width, height, num_stories):
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


def create_glowstone(x, y, z, length, width, height, num_stories):
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

def create_flowerpot(x, y, z, length, width, height, num_stories):
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
    
def create_overheadshelf(x, y, z, length, width, height, num_stories):
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
        



def create_wallshelf(x, y, z, length, width, displacement, height, num_stories):
    air = 0
    slab_colour = randint(8,13)
    random_l = randint(0, length)
    random_w = randint(0, width)
    if length < width: ## Length > Width of original rectangle 
            # Placing Shelves
            if mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + random_w) == air and mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 2 + random_w) == air and mc.getBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 1 + random_w) == air :
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + random_w, block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 1 + random_w , block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 2, z + 2 + random_w , block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + length + (1 * displacement), y + height * (num_stories - 1) + (num_stories - 1) + 3, z + random_w , 84)
    
    else: ## Width > Length of original rectangle 
        if mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement)) == air and mc.getBlock(x + 5 + 2 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement)) == air and mc.getBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement)) == air :
                mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement), block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + 1 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement), block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + 2 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 2, z + width + (1 * displacement), block.WOODEN_SLAB.withData(slab_colour))
                mc.setBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1) + 3, z + width + (1 * displacement), 84)

def create_piano(x, y, z, length, width, height, num_stories):
    random_l = randint(0, length)
    random_w = randint(0, width)
    stone_pressurep = 70
    jukebox = 84
    air = 0
    timeout = 0
    
    while mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + 4 + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 1 + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 3 + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1) + 1, z + 2 + random_w) != air or mc.getBlock(x + 5 + random_l + 1, y + height * (num_stories - 1) + (num_stories - 1), z + 2 + random_w) != air or mc.getBlock(x + 5 + random_l, y + height * (num_stories - 1) + (num_stories - 1), z + 2 + random_w) != air:
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