from mcpi.minecraft import Minecraft
from mcpi import block
from random import *
import random

from environment.coord import Coord
from plots.plot import Plot
from structures.furniture import *

# Roof design 1
def roof_design_1(num_stories):
    roof_start = height * num_stories + (num_stories - 1)
    min_size = min(length, width) // 3
    for i in range(0, min_size):
        
        mc.setBlocks(x + 4 + i, y + roof_start + i, z - 1 + i, x + 6 + length - i, y + roof_start + i, z - 1 + i,
                        164,
                        2)
        mc.setBlocks(x + 4 + i, y + roof_start + i, z + width + 1 - i, x + 6 + length - i, y + roof_start + i,
                        z + width + 1 - i, 164, 3)
        mc.setBlocks(x + 4 + i, y + roof_start + i, z + i, x + 4 + i, y + roof_start + i, z + width - i, 164, 0)
        mc.setBlocks(x + 6 + length - i, y + roof_start + i, z + i, x + 6 + length - i, y + roof_start + i,
                        z + width - i, 164, 1)

        if i == min_size - 1:
            
            mc.setBlocks(x + 4 + i + 1, y + roof_start + i, z - 1 + i + 1, x + 6 + length - i - 1,
                            y + roof_start + i,
                            z + width - i, 5, 5)

    if num_stories > 1:
        
        mc.setBlocks(x + 4, y + height, z - 1, x + 4, y + height, z + width + 1, wall_block)
        mc.setBlocks(x + 5 + length + 1, y + height, z - 1, x + 5 + length + 1, y + height, z + width + 1,
                        wall_block)
        mc.setBlocks(x + 4, y + height, z - 1, x + 5 + length + 1, y + height, z - 1, wall_block)
        mc.setBlocks(x + 4, y + height, z + width + 1, x + 5 + length + 1, y + height, z + width + 1, wall_block)

# Roof design 2
def roof_design_2(num_stories):
    i = num_stories - 1
    j = num_stories - 2

    
    mc.setBlocks(x + 4, y - 1, z - 1, x + 4, y + (height * num_stories) + num_stories, z - 1, pillar_block)
    mc.setBlocks(x + 5 + length + 1, y - 1, z - 1, x + 5 + length + 1, y + (height * num_stories) + num_stories,
                    z - 1,
                    pillar_block)
    mc.setBlocks(x + 4, y - 1, z + width + 1, x + 4, y + (height * num_stories) + num_stories, z + width + 1,
                    pillar_block)
    mc.setBlocks(x + 5 + length + 1, y - 1, z + width + 1, x + 5 + length + 1,
                    y + (height * num_stories) + num_stories,
                    z + width + 1, pillar_block)

    if num_stories > 1:
        for k in range(num_stories):
            
            mc.setBlocks(x + 4, y + (height * i) + j, z - 1, x + 4, y + (height * i) + j, z + width + 1,
                            pillar_block)
            mc.setBlocks(x + 5 + length + 1, y + (height * i) + j, z - 1, x + 5 + length + 1, y + (height * i) + j,
                            z + width + 1, pillar_block)
            mc.setBlocks(x + 4, y + (height * i) + j, z - 1, x + 5 + length + 1, y + (height * i) + j, z - 1,
                            pillar_block)
            mc.setBlocks(x + 4, y + (height * i) + j, z + width + 1, x + 5 + length + 1, y + (height * i) + j,
                            z + width + 1, pillar_block)

            i += 1
            j += 2
    else:
        
        mc.setBlocks(x + 4, y + height + 1, z - 1, x + 4, y + height + 1, z + width + 1, pillar_block)
        mc.setBlocks(x + 5 + length + 1, y + height + 1, z - 1, x + 5 + length + 1, y + height + 1, z + width + 1,
                        pillar_block)
        mc.setBlocks(x + 4, y + height + 1, z - 1, x + 5 + length + 1, y + height + 1, z - 1, pillar_block)
        mc.setBlocks(x + 4, y + height + 1, z + width + 1, x + 5 + length + 1, y + height + 1, z + width + 1,
                        pillar_block)

# Roof design 3
def roof_design_3(num_stories):
    i = num_stories - 1

    # Wood pillars
    
    mc.setBlocks(x + 5, y - 1, z, x + 5, y + (height * num_stories) + num_stories - 1, z, pillar_block)
    mc.setBlocks(x + 5 + length, y - 1, z, x + 5 + length, y + (height * num_stories) + num_stories - 1, z,
                    pillar_block)
    mc.setBlocks(x + 5, y - 1, z + width, x + 5, y + (height * num_stories) + num_stories - 1, z + width,
                    pillar_block)
    mc.setBlocks(x + 5 + length, y - 1, z + width, x + 5 + length, y + (height * num_stories) + num_stories - 1,
                    z + width, pillar_block)

    if num_stories > 1:
        
        mc.setBlocks(x + 4, y + height, z - 1, x + 4, y + height, z + width + 1, pillar_block)
        mc.setBlocks(x + 5 + length + 1, y + height, z - 1, x + 5 + length + 1, y + height, z + width + 1,
                        pillar_block)
        mc.setBlocks(x + 4, y + height, z - 1, x + 5 + length + 1, y + height, z - 1, pillar_block)
        mc.setBlocks(x + 4, y + height, z + width + 1, x + 5 + length + 1, y + height, z + width + 1, pillar_block)

    
    mc.setBlocks(x + 4, y + (height * num_stories) + i, z - 1, x + 4, y + (height * num_stories) + i, z + width + 1,
                    126, 13)
    mc.setBlocks(x + 5 + length + 1, y + (height * num_stories) + i, z - 1, x + 5 + length + 1,
                    y + (height * num_stories) + i, z + width + 1, 126, 13)
    mc.setBlocks(x + 4, y + (height * num_stories) + i, z - 1, x + 5 + length + 1, y + (height * num_stories) + i,
                    z - 1, 126, 13)
    mc.setBlocks(x + 4, y + (height * num_stories) + i, z + width + 1, x + 5 + length + 1,
                    y + (height * num_stories) + i, z + width + 1, 126, 13)

    mc.setBlocks(x + 5, y + (height * num_stories) + num_stories, z, x + 5 + length,
                    y + (height * num_stories) + num_stories, z + width, 126, 5)

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
            
            mc.setBlocks(x + 5 + place_wall, y + height * (num_stories - 1), z, x + 5 + place_wall,
                            y + height * num_stories, z + width, wall_block)

            # Add doorway
            
            mc.setBlocks(x + 5 + place_wall, y + (height * (num_stories - 1)) + (num_stories - 1), z + width // 2,
                            x + 5 + place_wall, y + (height * (num_stories - 1)) + num_stories, z + width // 2,
                            block.AIR)
            
            ## allows for placement of default items ##
            positive_room = 1
            negative_room = -1

            # Places items into the bottom half because it is a bigger room
            if place_wall > room_midpoint:
                create_big_room(x, y, z, place_wall, width, negative_room, height, num_stories)
            # Places items into the top half because it is a bigger
            else:
                create_big_room(x, y, z, place_wall, width, positive_room, height, num_stories)

            # 2/3 chance to generate another room
            room_chance = random.randint(1, 4)
            if room_chance == 2 or room_chance == 3:
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
            
            mc.setBlocks(x + 5, y + height * (num_stories - 1), z + place_wall, x + 5 + length,
                            y + height * num_stories, z + place_wall, wall_block)

            # Add a doorway
            
            mc.setBlocks(x + 5 + length // 2, y + (height * (num_stories - 1)) + (num_stories - 1), z + place_wall,
                            x + 5 + length // 2, y + (height * (num_stories - 1)) + num_stories, z + place_wall,
                            block.AIR)
            
            positive_room = 1
            negative_room = -1
            
            # Places items into the left half because it is a bigger room
            if place_wall > room_midpoint:
                create_big_room(x, y, z, length, place_wall, negative_room, height, num_stories)
            # Places items into the right half because it is a bigger
            else:
                create_big_room(x, y, z, length, place_wall, positive_room, height, num_stories)

            # 2/3 chance to generate another room
            room_chance = random.randint(1, 3)
            if room_chance == 2 or room_chance == 3:
                generate_rooms(x, y, z, length, place_wall, height, num_stories)
            else: # This is to generate the second room 
                # Places items into the right half because it is a smaller room
                if place_wall > room_midpoint:
                    create_small_room(x, y, z, length, place_wall, positive_room, height, num_stories)
                # Places items into the left half because it is a smaller 
                else:
                    create_small_room(x, y, z, length, place_wall, negative_room, height, num_stories)

# Generate staircase if num_stories > 1
def generate_stairs(x, y, z, height):
    
    mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1, block.AIR)

    # Place wood pillar
    mc.setBlocks(x, y, z, x, y + (height * 2), z, 17, 12)

    if door_flag_north == True:
        
        mc.setBlock(x - 1, y, z + 1, 126, 5)
        mc.setBlock(x - 1, y, z, 126, 13)
        mc.setBlock(x - 1, y + 1, z - 1, 126, 5)
        mc.setBlock(x, y + 1, z - 1, 126, 13)
        mc.setBlock(x + 1, y + 2, z - 1, 126, 5)
        mc.setBlock(x + 1, y + 2, z, 126, 13)
        mc.setBlock(x + 1, y + 3, z + 1, 126, 5)
        mc.setBlock(x, y + 3, z + 1, 126, 13)
        mc.setBlock(x - 1, y + 4, z + 1, 126, 5)
        mc.setBlock(x - 1, y + 4, z, 126, 13)

    elif door_flag_south == True:
        
        mc.setBlock(x + 1, y, z - 1, 126, 5)
        mc.setBlock(x + 1, y, z, 126, 13)
        mc.setBlock(x + 1, y + 1, z + 1, 126, 5)
        mc.setBlock(x, y + 1, z + 1, 126, 13)
        mc.setBlock(x - 1, y + 2, z + 1, 126, 5)
        mc.setBlock(x - 1, y + 2, z, 126, 13)
        mc.setBlock(x - 1, y + 3, z - 1, 126, 5)
        mc.setBlock(x, y + 3, z - 1, 126, 13)
        mc.setBlock(x + 1, y + 4, z - 1, 126, 5)
        mc.setBlock(x + 1, y + 4, z, 126, 13)

    elif door_flag_east == True:
        
        mc.setBlock(x - 1, y, z - 1, 126, 5)
        mc.setBlock(x, y, z - 1, 126, 13)
        mc.setBlock(x + 1, y + 1, z - 1, 126, 5)
        mc.setBlock(x + 1, y + 1, z, 126, 13)
        mc.setBlock(x + 1, y + 2, z + 1, 126, 5)
        mc.setBlock(x, y + 2, z + 1, 126, 13)
        mc.setBlock(x - 1, y + 3, z + 1, 126, 5)
        mc.setBlock(x - 1, y + 3, z, 126, 13)
        mc.setBlock(x - 1, y + 4, z - 1, 126, 5)
        mc.setBlock(x, y + 4, z - 1, 126, 13)

    elif door_flag_west == True:
        
        mc.setBlock(x + 1, y, z + 1, 126, 5)
        mc.setBlock(x, y, z + 1, 126, 13)
        mc.setBlock(x - 1, y + 1, z + 1, 126, 5)
        mc.setBlock(x - 1, y + 1, z, 126, 13)
        mc.setBlock(x - 1, y + 2, z - 1, 126, 5)
        mc.setBlock(x, y + 2, z - 1, 126, 13)
        mc.setBlock(x + 1, y + 3, z - 1, 126, 5)
        mc.setBlock(x + 1, y + 3, z, 126, 13)
        mc.setBlock(x + 1, y + 4, z + 1, 126, 5)
        mc.setBlock(x, y + 4, z + 1, 126, 13)


# rect_bottom_left, rect_top_right = plot.getCoordsForHouse()
# x, y, z = rect_bottom_left.x - 5, rect_bottom_left.y + 1, rect_bottom_left.z
mc = Minecraft.create()
x, y, z = mc.player.getPos()

# Choosing a random block type for the walls/floors/pillars
palette_1 = [155, block.COBBLESTONE, block.STONE_BRICK]
palette_2 = [block.STONE_BRICK, block.WOOD_PLANKS, 17]
palette_3 = [block.BRICK_BLOCK, 1, block.COBBLESTONE]

palette_list = []
palette_list.append(palette_1)
palette_list.append(palette_2)
palette_list.append(palette_3)

choose_palette = random.choice(palette_list)
wall_block = choose_palette[0]
floor_block = choose_palette[1]
pillar_block = choose_palette[2]

# Randomly set length, width and height of house
length = random.randint(15, 17)
height = 4
width = random.randint(15, 17)

# Generate the walls
mc.setBlocks(x + 5, y, z, x + 5 + length, y + height, z + width, wall_block)
mc.setBlocks(x + 6, y, z + 1, x + 5 + length - 1, y + height - 1, z + width - 1, block.AIR)

# Generate the floors
mc.setBlocks(x + 5, y - 1, z, x + 5 + length, y - 1, z + width, floor_block)

# Generate windows
mc.setBlocks(x + 5 + 2, y + 1, z, x + 5 + length - 2, y + height - 2, z, block.GLASS)
mc.setBlocks(x + 5 + 2, y + 1, z + width, x + 5 + length - 2, y + height - 2, z + width, block.GLASS)
mc.setBlocks(x + 5, y + 1, z + 2, x + 5, y + height - 2, z + width - 2, block.GLASS)
mc.setBlocks(x + 5 + length, y + 1, z + 2, x + 5 + length, y + height - 2, z + width - 2, block.GLASS)

# Generate door
choose_wall = random.randint(2, 2)

door_x, door_z = 0, 0
door_flag_north = False
door_flag_east = False
door_flag_south = False
door_flag_west = False

if choose_wall == 1:
    wall = random.randint(1, 2)
    set_door = length // 2
    if wall == 1:  # West
        
        mc.setBlocks(x + 5 + set_door - 1, y, z, x + 5 + set_door + 1, y + 3, z, wall_block)
        mc.setBlock(x + 5 + set_door, y + 1, z, 64, 8)
        mc.setBlock(x + 5 + set_door, y, z, 64, 1)
        door_flag_west = True
        door_x = x+5+set_door
        door_z = z
        door_z -= 1


    elif wall == 2:  # East
        
        mc.setBlocks(x + 5 + set_door - 1, y, z + width, x + 5 + set_door + 1, y + 3, z + width, wall_block)
        mc.setBlock(x + 5 + set_door, y + 1, z + width, 64, 8)
        mc.setBlock(x + 5 + set_door, y, z + width, 64, 0)
        door_flag_east = True
        door_x = x+5+set_door
        door_z = z+width
        door_z += 1


else:
    wall = random.randint(1, 1)
    set_door = width // 2
    if wall == 1:  # South
        mc.setBlocks(x + 5, y, z + set_door - 1, x + 5, y + 3, z + set_door + 1, wall_block)
        mc.setBlock(x + 5, y + 1, z + set_door, 64, 8)
        mc.setBlock(x + 5, y, z + set_door, 64, 0)
        door_flag_south = True
        door_x = x+5
        door_z = z+set_door
        door_x -= 1

    elif wall == 2:  # North
        mc.setBlocks(x + 5 + length, y, z + set_door - 1, x + 5 + length, y + 3, z + set_door + 1, wall_block)
        mc.setBlock(x + 5 + length, y + 1, z + set_door, 64, 9)
        mc.setBlock(x + 5 + length, y, z + set_door, 64, 7)
        door_flag_north = True
        door_x = x+5+length
        door_z = z+set_door
        door_x += 1

## To generate libary shelves ##
if door_flag_west == True:
    shelf_wall = [2,3]
    door_wall = 1
if door_flag_north == True:
    shelf_wall = [3,4]
    door_wall = 2
if door_flag_east == True:
    shelf_wall = [1,4]
    door_wall = 3
if door_flag_south == True:
    shelf_wall = [1,2]
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



## Generation of the flowers beds outside ##
if door_wall != 1:
# West
    flower = randint(0,7)
    
    mc.setBlocks(x + 5 + 2, y, z - 1, x + 5 + length - 2, y, z - 1, block.GRASS)
    mc.setBlocks(x + 5 + 2, y + 1, z - 1, x + 5 + length - 2, y + 1, z - 1, block.FLOWER_CYAN.withData(flower))

if door_wall != 3: # East
    # Left side of the house 
    flower = randint(0,7)
    mc.setBlocks(x + 5 + 2, y, z + width + 1, x + 5 + length - 2, y, z + width + 1, block.GRASS)
    mc.setBlocks(x + 5 + 2, y + 1, z + width + 1, x + 5 + length - 2, y + 1, z + width + 1, block.FLOWER_CYAN.withData(flower))
    
    
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

# Generate rooms
generate_rooms(x, y, z, length, width, height, 1)
place_items(x, y, z, length, width, height, 1)

# Generate random number of stories for the house
num_stories = random.randint(2, 2)

if num_stories == 1:
    choose_roof = random.randint(1, 3)
    if choose_roof == 1:
        roof_design_1(num_stories)
    elif choose_roof == 2:
        roof_design_2(num_stories)
    else:
        roof_design_3(num_stories)

else:
    i = 1
    j = 2
    k = 0

    while i < num_stories:
        # Generate the walls
        
        mc.setBlocks(x + 5, y + height * i + i, z, x + 5 + length, y + height * j + i, z + width, wall_block)
        mc.setBlocks(x + 6, y + height * i, z + 1, x + 5 + length - 1, y + height * j + 1, z + width - 1, block.AIR)

        # Generate windows
        mc.setBlocks(x + 5 + 2, y + height * i + i + 1, z, x + 5 + length - 2, y + height * j + i - 2, z,
                        block.GLASS)
        mc.setBlocks(x + 5 + 2, y + height * i + i + 1, z + width, x + 5 + length - 2, y + height * j + i - 2,
                        z + width, block.GLASS)
        mc.setBlocks(x + 5, y + height * i + i + 1, z + 2, x + 5, y + height * j + i - 2, z + width - 2,
                        block.GLASS)
        mc.setBlocks(x + 5 + length, y + height * i + i + 1, z + 2, x + 5 + length, y + height * j + i - 2,
                        z + width - 2, block.GLASS)

        # Generate rooms for the floor
        generate_rooms(x, y, z, length, width, height, num_stories)
        place_items(x, y, z, length, width, height, num_stories)

        # Generate the floors
        mc.setBlocks(x + 6, y + height * i + k, z + 1, x + 5 + length - 1, y + height * i + k, z + width - 1,
                        floor_block)

        i += 1
        j += 1
        k += 1

    # Call generate stairs function depending on where door is
    if door_flag_south == True:
        generate_stairs(x + 7, y, z + width - 2, height)

    elif door_flag_west == True:
        generate_stairs(x + 7, y, z + 2, height)

    elif door_flag_north == True:
        generate_stairs(x + 5 + length - 2, y, z + 2, height)

    elif door_flag_east == True:
        generate_stairs(x + 5 + length - 2, y, z + width - 2, height)

    # choose_roof = random.randint(1, 3)
    # if choose_roof == 1:
    #     roof_design_1(num_stories)
    # elif choose_roof == 2:
    #     roof_design_2(num_stories)
    # else:
    #     roof_design_3(num_stories)