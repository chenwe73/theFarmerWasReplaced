import utils

cols, rows = 4, 8
w = get_world_size() // cols
h = get_world_size() // rows

ent = Entities.Sunflower
item = Items.Power
min_petal, max_petal = 7, 15
min_water = 0.9

def setup():
    x, y = get_pos_x(), get_pos_y()
    for i in range(5):
        for j in range(2):
            utils.move_to(x+i, y+j)
            if get_ground_type() == Grounds.Grassland:
                till()
            if get_entity_type() == None:
                plant(ent)
                while measure() > min_petal:
                    harvest()
                    plant(ent)

def drone():
    x, y = get_pos_x(), get_pos_y()
    if get_ground_type() == Grounds.Grassland:
        till()
    stats = {"items": num_items(item), "time": get_time()}
    while True:
        if can_harvest():
            harvest()
            stats = {"items": num_items(item), "time": get_time()}
        if get_entity_type() == None:
            plant(ent)
        while get_water() < min_water:
            use_item(Items.Water)
        if num_items(Items.Fertilizer) > 0 and num_items(Items.Weird_Substance) > 0:
            use_item(Items.Fertilizer)
            use_item(Items.Weird_Substance)

def main():
    for i in range(cols):
        for j in range(rows):
            utils.move_to(i * w, j * h)
            if (i, j) == (cols-1, rows-1):
                break
            spawn_drone(drone)

    x, y = get_pos_x(), get_pos_y()
    utils.move_to(x, y)
    setup()
    drone()


if __name__ == "__main__":
    main()
