import utils
import cactus
import dino
import maze
import power
import pumpkin

# size = get_world_size()
size = 8
min_water = 0.75


def grow(ent):
    if ent == Entities.Grass:
        return
    if get_ground_type() == Grounds.Grassland:
        till()
    if get_entity_type() != None:
        if not can_harvest():
            quick_print(get_pos_x(), get_pos_y(), get_entity_type())
        return
    plant(ent)
    if ent == Entities.Tree:
        use_item(Items.Fertilizer)
    while get_water() < min_water:
        use_item(Items.Water)

def basic():
    rows, cols = 4, 8
    x, y = get_pos_x(), get_pos_y()
    while True:
        for i in range(cols):
            for j in range(rows):
                utils.move_to(x+i, y+j)
                if can_harvest():
                    harvest()
                if i % 2 == 0 and j % 2 == 0:
                    ent = Entities.Tree
                elif i % 2:
                    ent = Entities.Carrot
                else:
                    ent = Entities.Grass
                grow(ent)

def parallel():
    cols, rows = 4, 8
    w = get_world_size() // cols
    h = get_world_size() // rows
    for i in range(cols):
        for j in range(rows):
            utils.move_to(i * w, j * h)
            if (i, j) == (cols-1, rows-1):
                break
            spawn_drone(maze)
        move(East)

def sim():
    sim_items = {}
    for item in Items:
        sim_items[item] = 1000000
    simulate("power", Unlocks, sim_items, {}, 0, 10)

def main():
	clear()
	change_hat(Hats.Top_Hat)

	# parallel()
	# utils.dino()
	# cactus.main()
	# maze.main()
	# pumpkin.main()
	power.main()

	# sim()
	# leaderboard_run(Leaderboards.Maze_Single, "maze", 1000)


if __name__ == "__main__":
    main()
